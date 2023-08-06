import requests
from lxml import etree
from prettytable import PrettyTable


def queryIP(ip):
    try:
        url = "https://ip.chinaz.com/{}".format(ip)

        headers = {
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
        data = {"ip": ip}
        headers["Host"] = "ip.chinaz.com"
        res = requests.post(url=url, data=data, headers=headers).text
        etree_html = etree.HTML(res)
        a = etree_html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/span[1]/text()')[0]  # 域名/IP
        b = etree_html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/span[2]/text()')[0]  # 获取的IP地址
        c = etree_html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/span[3]/text()')[0]  # 数字地址
        d = etree_html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/span[4]/text()')[0]  # 运营商
        e = etree_html.xpath('/html/body/div[2]/div[1]/div[3]/div[2]/div[2]/span[5]/em/text()')[0]  # IP的物理位置
        table = PrettyTable(["域名/IP", "获取的IP地址", "数字地址", "运营商", "IP的物理位置"])
        table.title = '\033[1;34;34m' + "queryIP" + '\033[0m'
        table.add_row([a, b, c, d, e])
        print(table)
    except:
        print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')

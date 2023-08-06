import requests
from prettytable import PrettyTable
from lxml import etree


def queryPhoneNum(Num):
    try:
        url = "https://www.haoshudi.com/{}.htm".format(Num)
        headers = {
            "Host": "www.haoshudi.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)Gecko/20100101 Firefox/112.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Referer": "https://www.haoshudi.com/",
            "sec-ch-ua-platform": "Windows",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"}
        res = requests.get(url=url, headers=headers).text
        etree_html = etree.HTML(res)
        b = etree_html.xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/a[1]/text()')[0]  # 省
        c = etree_html.xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[2]/td[2]/span/a[2]/text()')[0]  # 市
        d = etree_html.xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[3]/td[2]/span/a/text()')[0]  # 运营商
        e = etree_html.xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[4]/td[2]/span/a/text()')[0]  # 电话区号
        f = etree_html.xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[5]/td[2]/span/a/text()')[0]  # 邮编
        g = etree_html.xpath('/html/body/div[1]/div[2]/div/div[1]/div[2]/table/tbody/tr[6]/td[2]/span/text()')[0]  # 区划代码
        table = PrettyTable(["手机号码", "归属地", "运营商", "电话区号", "邮编", "区划代码"])
        table.title = '\033[1;34;34m' + "queryPhoneNum" + '\033[0m'
        table.add_row([Num, b + c, d, e, f, g])
        print(table)
    except:
        print('\033[1;31;31m' + "[-] Execution failed." + '\033[0m')

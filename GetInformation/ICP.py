import requests
from lxml import etree
from prettytable import PrettyTable


def ICP(domain):
    try:
        url = "https://icp.chinaz.com/{}".format(domain)
        url2 = "https://seo.chinaz.com/{}".format(domain)

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
        data = {"keyword": domain}
        headers["Host"] = "icp.chinaz.com"
        res = requests.post(url=url, data=data, headers=headers).text
        etree_html = etree.HTML(res)
        a = etree_html.xpath('//*[@id="companyName"]/text()')[0]  # 主办单位名称
        b = etree_html.xpath('//*[@id="first"]/li[2]/p/strong/text()')[0]  # 主办单位性质
        c = etree_html.xpath('//*[@id="first"]/li[4]/p/text()')[0]  # 网站名称
        d = etree_html.xpath('//*[@id="first"]/li[6]/p/text()')[0]  # 网站首页网址
        e = etree_html.xpath('//*[@id="first"]/li[8]/p/text()')[0]  # 审核时间
        headers["Host"] = "seo.chinaz.com"
        res = requests.get(url2, headers).text
        etree_html = etree.HTML(res)
        f = etree_html.xpath('/html/body/div[4]/table/tbody/tr[4]/td[2]/span[1]/i/a/text()')[0]  # 网站备案/许可证号
        table = PrettyTable(["主办单位名称", "主办单位性质", "网站名称", "网站首页网址", "审核时间", "网站备案/许可证号"])
        table.title = '\033[1;34;34m' + "ICP" + '\033[0m'
        table.add_row([a, b, c, d, e, f])
        print(table)
    except:
        print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')

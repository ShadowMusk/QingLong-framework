import requests
import json
from prettytable import PrettyTable


def queryIDcard(IdCard):
    try:
        url = "https://www.haoshudi.com/api/id/query/?userid={}".format(IdCard)
        headers = {
            "Host": "www.haoshudi.com",
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:109.0)Gecko/20100101 Firefox/112.0",
            "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,*/*;q=0.8",
            "Accept-Language": "zh-CN,zh;q=0.8,zh-TW;q=0.7,zh-HK;q=0.5,en-US;q=0.3,en;q=0.2",
            "Accept-Encoding": "gzip, deflate",
            "Connection": "close",
            "Referer": "https://www.haoshudi.com/shenfenzheng/",
            "sec-ch-ua-platform": "Windows",
            "Upgrade-Insecure-Requests": "1",
            "Sec-Fetch-Dest": "document",
            "Sec-Fetch-Mode": "navigate",
            "Sec-Fetch-Site": "none",
            "Sec-Fetch-User": "?1"}
        res = requests.get(url=url, headers=headers).text
        json_string = res
        data = json.loads(json_string)
        table = PrettyTable(["sex", "birthday", "address", "newAddress", "zodiac", "starsign", "isIdCard"])
        table.title = '\033[1;34;34m' + "queryIDcard" + '\033[0m'
        table.add_row([data["data"]["sex"], data["data"]["birthday"], data["data"]["address"], data["data"]["newAddress"], data["data"]["zodiac"], data["data"]["starsign"], data["data"]["isIdCard"]])
        print(table)
    except:
        print('\033[1;31;31m' + "[-] {}".format(data["msg"]) + '\033[0m')

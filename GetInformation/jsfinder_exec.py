import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
from prettytable import PrettyTable


def myjsfinder():
    commands = ["back", "JSFinder.py", "how to use JSFinder.py"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mJSFinder > \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice == 'back':
            break
        elif choice == "how to use JSFinder.py":
            jsfinder_help()
            continue
        elif choice == "":
            continue
        os.system("python3 " + choice)
        continue


def jsfinder_help():
    table = PrettyTable(["parameter", "description"])  # 实例化对象
    table.add_rows([
        ["-u,--url", "目标网站"],
        ["-c,--cookie", "目标网站的cookie"],
        ["-f,--file", "包含url或者js的文件"],
        ["-ou,--outputurl", "输出url的文件名称"],
        ["-os,--outputsubdomain", "输出子域名的文件名称"],
        ["-j,--js", "在js文件中爬取"],
        ["-d,--deep", "深度爬取"]
    ])
    table_string = table.get_string()
    table_width = len(table_string.splitlines()[0])
    title = "Ways to use JSFinder"
    print(f"{title:^{table_width}}")
    # print(table)  # 把表格输出
    print(table_string)
    print("======================== EXAMPLES =======================")
    print("JSFinder.py -u http://www.mi.com")
    print("JSFinder.py -u http://www.mi.com -d")
    print("JSFinder.py -u http://www.mi.com -d -ou mi_url.txt -os mi_subdomain.txt")
    print("JSFinder.py -f text.txt")
    print("JSFinder.py -f text.txt -j")
    print('JSFinder.py -u http://www.mi.com -c "session=xxx"')
    print("JSFinder.py -u http://www.mi.com -ou mi_url.txt")
    print("JSFinder.py -u http://www.mi.com -os mi_subdomain.txt")

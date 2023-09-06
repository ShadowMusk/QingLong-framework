import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
import GetDomainsInformation
import Wafw00f
import Dirb
import Nmap
import jsfinder_exec


class GetInformation:
    def __init__(self):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Information Gathering) > \033[0m')
        history = InMemoryHistory()
        while True:
            choice = prompt(formatted_text1, completer=completer, history=history)
            if choice == '1':
                domains_information = GetDomainsInformation.DomainInformation()
            elif choice == '2':
                Wafw00f.mywafw00f()
                continue
            elif choice == '3':
                Dirb.mydirb()
                continue
            elif choice == '4':
                Nmap.mynmap()
                continue
            elif choice == '5':
                jsfinder_exec.myjsfinder()
                continue
            elif choice == 'back':
                break
            elif choice == 'show functions':
                self.show_functions()
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Information Gathering" + '\033[0m' + "\n" + '=' * len("Information Gathering") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Domain name information collection", "1", "信息收集"],
                  ["2", "WAF Identification", "2", "WAF识别"], ["3", "Directory Scan", "3", "目录扫描"], ["4", "Nmap", "4", "Nmap扫描"], ["5", "JSFinder", "5", "在网站的js文件中提取URL和子域名"]]
        MyTable.createTable(headers, mydata)

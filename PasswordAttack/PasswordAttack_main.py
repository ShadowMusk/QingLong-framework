import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
import hydra
import medusa
import hashcat
import john


class PasswordAttacks:
    def __init__(self):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Password Attacks) > \033[0m')
        while True:
            choice = prompt(formatted_text1, completer=completer)
            if choice == 'back':
                break
            elif choice == 'show functions':
                self.show_functions()
                continue
            elif choice == '1':
                hydra.myhydra()
                continue
            elif choice == '2':
                medusa.mymedusa()
                continue
            elif choice == '3':
                hashcat.myhashcat()
                continue
            elif choice == '4':
                john.myjohn()
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Malicious Attacks" + '\033[0m' + "\n" + '=' * len("Malicious Attacks") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "hydra", "1", "利用hydra爆破密码"], ["2", "medusa", "2", "利用medusa爆破密码"], ["3", "hashcat", "3", "利用hashcat爆破密码"], ["4", "john", "4", "利用john爆破密码"]]
        MyTable.createTable(headers, mydata)

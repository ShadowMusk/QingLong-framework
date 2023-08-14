import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable


class DDoS:
    def __init__(self):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Denial of Service) > \033[0m')
        history = InMemoryHistory()
        while True:
            choice = prompt(formatted_text1, completer=completer, history=history)
            if choice == 'back':
                break
            elif choice == 'show functions':
                self.show_functions()
                continue
            elif choice == '1':
                self.hping3()
                continue
            elif choice == '2':
                self.slowloris()
                continue
            elif choice == '3':
                self.goldeneye()
                continue
            elif choice == '4':
                self.hammer()
                continue
            elif choice == '5':
                self.DDos_Attack()
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Denial of Service Attacks" + '\033[0m' + "\n" + '=' * len("Denial of Service Attacks") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "hping3", "1", "利用hping3发起拒绝服务攻击"], ["2", "slowloris", "2", "利用slowloris发起拒绝服务攻击"], ["3", "goldeneye", "3", "利用goldeneye发起拒绝服务攻击"],
                  ["4", "hammer", "4", "利用hammer发起拒绝服务攻击"], ["5", "DDos-Attack", "5", "利用DDos-Attack发起拒绝服务攻击"]]
        MyTable.createTable(headers, mydata)

    def hping3(self):
        commands = ["back", "help", "sudo hping3"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32mhping3 > \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'help':
                    os.system("sudo hping3 -h")
                    continue
                os.system(choice)
                continue
            except KeyboardInterrupt:
                continue
            except:
                print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
                continue

    def slowloris(self):
        commands = ["back", "help", "slowloris.py"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32mslowloris > \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'help':
                    os.system("python3  slowloris.py -h")
                    continue
                command = "python3 " + choice
                os.system(command)
                continue
            except KeyboardInterrupt:
                continue
            except:
                print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
                continue

    def goldeneye(self):
        commands = ["back", "help", "goldeneye.py"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32mgoldeneye > \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'help':
                    os.system("python3  goldeneye.py -h")
                    continue
                command = "python3 " + choice
                os.system(command)
                continue
            except KeyboardInterrupt:
                continue
            except:
                print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
                continue

    def hammer(self):
        commands = ["back", "help", "hammer.py"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32mhammer > \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'help':
                    os.system("python3  hammer.py -h")
                    continue
                command = "python3 " + choice
                os.system(command)
                continue
            except KeyboardInterrupt:
                continue
            except:
                print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
                continue

    def DDos_Attack(self):
        commands = ["back", "help", "ddos_attack.py"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32mDDos_Attack > \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'help':
                    os.system("python3  ddos_attack.py -h")
                    continue
                command = "python3 " + choice
                os.system(command)
                continue
            except KeyboardInterrupt:
                continue
            except:
                print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
                continue

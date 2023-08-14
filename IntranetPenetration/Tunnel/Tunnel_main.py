import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from IntranetPenetration.Tunnel.Netsh import Netsh
from IntranetPenetration.Tunnel.ICMP_Tunnel import ICMP_Tunnel
from AuxiliaryFunctions import MyTable


class Tunnel:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Tunnel] \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer,history=history)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == "":
                    continue
                elif choice.split()[0] == '1':
                    ICMP_Tunnel.ICMP_Tunnel(choice)
                    continue
                elif choice == '2':
                    Netsh.Netsh(conn)
                    continue
                elif choice == 'back':
                    break
                elif choice == 'show params':
                    self.show_params()
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["victim_ip", "受害者IP"], ["localport", "本地监听端口"], ["target_ip", "目标主机的IP"], ["target_port", "目标端口"], ["password", "隧道密码"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Tunnel" + '\033[0m' + "\n" + '=' * len("Tunnel") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "ICMP Tunnel", "1 victim_ip localport target_ip target_port password", "ICMP隧道"],
                  ["2", "Netsh", "2", "Netsh端口转发"]]
        MyTable.createTable(headers, mydata)

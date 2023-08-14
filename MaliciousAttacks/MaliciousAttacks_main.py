import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from AuxiliaryFunctions import MyTable
import PhishingEmails
import EmailBombing


class MaliciousAttacks:
    def __init__(self):
        commands = ["back", "show functions"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Malicious Attacks) > \033[0m')
        history = InMemoryHistory()
        while True:
            try:
                choice = prompt(formatted_text1, completer=completer,history=history)
                if choice == 'back':
                    break
                elif choice == "":
                    continue
                elif choice == 'show functions':
                    self.show_functions()
                    continue
                elif choice == '1':
                    phishing_emails = PhishingEmails.PhishingEmails()
                    continue
                elif choice == '2':
                    email_bombing = EmailBombing.EmailBombing()
                    continue
            except IndexError:
                print('\033[1;31;31m' + "[-] You need to offer other params." + '\033[0m')
                continue

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Malicious Attacks" + '\033[0m' + "\n" + '=' * len("Malicious Attacks") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [
            ["1", "Phishing emails", "1", "邮件钓鱼"],
            ["2", "Email Bombing", "2", "邮件轰炸"]]
        MyTable.createTable(headers, mydata)


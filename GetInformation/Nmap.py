import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
import nmap_help


def mynmap():
    commands = ["back", "how to use nmap", "nmap"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mnmap > \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice == 'back':
            break
        elif choice == "":
            continue
        elif choice == 'how to use nmap':
            nmap_help.help()
            continue
        os.system(choice)
        continue

import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import john_help


def myjohn():
    commands = ["back", "how to use john", "john"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mjohn > \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice == 'back':
            break
        elif choice == 'how to use john':
            john_help.help()
            continue
        os.system(choice)
        continue

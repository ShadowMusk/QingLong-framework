import os
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory


def mywafw00f():
    commands = ["back", "wafw00f"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mwafw00f > \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice == 'back':
            break
        elif choice == "":
            continue
        os.system(choice)
        continue

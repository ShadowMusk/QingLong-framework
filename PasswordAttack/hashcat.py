import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))


def myhashcat():
    commands = ["back", "hashcat"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mhashcat > \033[0m')
    while True:
        choice = prompt(formatted_text1, completer=completer)
        if choice == 'back':
            break
        os.system(choice)
        continue

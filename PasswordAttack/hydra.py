import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
import hydra_help


def myhydra():
    commands = ["back", "how to use hydra", "hydra"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32mhydra > \033[0m')
    while True:
        choice = prompt(formatted_text1, completer=completer)
        if choice == 'back':
            break
        elif choice == 'how to use hydra':
            hydra_help.help()
            continue
        os.system(choice)
        continue

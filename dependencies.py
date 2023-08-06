import os

print('\033[1;32;32m' + "[+] 正在安装所需环境依赖，请耐心等待.如果安装出现错误，请多重试几次." + '\033[0m')
tool_list = ["hydra", "medusa", "john", "nikto", "nmap", "wafw00f", "sqlmap", "hashcat", "wapiti", "dirb", "rdesktop"]
os.system("pip3 install -r myrequirements.txt")


def install(tool_name):
    # 先尝试使用 apt-get 来安装
    apt_get_result = os.system("sudo apt-get install {}".format(tool_name))
    if apt_get_result == 0:  # apt-get 命令成功执行
        return
    # 如果 apt-get 安装失败，再尝试使用 yum 来安装
    yum_result = os.system("sudo yum install {}".format(tool_name))
    if yum_result == 0:  # yum 命令成功执行
        return
    # 如果 yum 安装失败，打印错误信息
    print('\033[1;32;32m' + "[-] Failed to install {} with both apt-get and yum.".format(tool_name) + '\033[0m')


for t in tool_list:
    install(t)

# Update Records

## 1.QingLong Framework v1.1 updated on August 8, 2023

The updated content of this version is as follows:

When we engage in email phishing and email bombing attacks, the framework allows us to customize the sender and receiver.

（当我们进行邮箱钓鱼和邮箱轰炸攻击时，允许我们自定义发件人和接收人。）

该功能在恶意攻击模块。

## 2.QingLong Framework v1.2 updated on August 9, 2023

The updated content of this version is as follows:

Allow attackers to steal passwords from Google Chrome.

（允许攻击者们盗取谷歌浏览器的密码。）

**首先需要注意：受害者主机上面的杀毒软件、防火墙等都要关闭！！！！！！**

该功能在内网渗透模块的小工具模块下。

使用方法：进入后门后，选择序号7进入小工具模块，接着选择”盗取谷歌浏览器的密码”的功能序号，执行“upload getChromePassword.exe”命令，把getChromePassword.exe上传到受害者主机，然后执行“run”命令即可。

步骤可参考：https://www.freebuf.com/sectool/374684.html

## 3.QingLong Framework v1.3 updated on August 10, 2023

The updated content of this version is as follows:

Allow attackers to obtain the victims' WiFi passwords.

（允许攻击者获取受害者的wifi密码。）

**首先需要注意：受害者主机上面的杀毒软件、防火墙等都要关闭！！！！！！**

该功能在内网渗透模块的小工具模块下。

使用方法：进入后门后，选择序号7进入小工具模块，接着选择“盗取wifi密码”的功能序号即可。

步骤可参考：https://www.freebuf.com/sectool/374684.html

## 4.QingLong Framework v1.4 updated on August 14, 2023

The updated content of this version is as follows:

Command line support for querying input history function.

（命令行支持通过上下键来选择历史命令。）

## 5.QingLong Framework v1.14 updated on August 25, 2023

1、优化内网渗透模块的权限提升模块。

2、集成powersploit框架的PowerUp.ps1的部分功能，后续还会继续集成PowerUp.ps1的其他功能，如下是其集成的功能：

（1）检查%PATH%是否存在当前用户可以写入的目录

（2）从系统上的applicationHost.config文件恢复加密过的应用池和虚拟目录的密码

（3）检查AlwaysInstallElevated注册表项是否被设置，如果被设置，意味着MSI文件是以system权限运行的

（4）检测Winlogin注册表AutoAdminLogon项有没有被设置，可查询默认的用户名和密码

（5）查找可能包含有部署凭据的文件

（6）检查开机自启的应用程序路径和注册表键值，返回当前用户可修改的程序路径

（7）返回当前用户能够修改的计划任务程序的名称和路径

（8）返回当前服务器上的web.config文件中的数据库连接字符串的明文

3、使用方法：**首先需要注意：受害者主机上面的杀毒软件、防火墙等都要关闭！！！！！！**连接后门，进入权限提升模块，选择序号1进入PowerUp.ps1模块，然后上传PowrUp.ps1（敲击tab键，选择“upload PowrUp.ps1”命令即可），然后就可以使用上述功能了。

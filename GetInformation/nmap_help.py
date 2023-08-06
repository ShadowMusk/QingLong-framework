def help():
    print("""
    Nmap 7.93 ( https://nmap.org )
    Usage: nmap [扫描类型] [选项] {目标规范}
    TARGET SPECIFICATION:
      可以传主机名,IP 地址,网络等
      例如: scanme.nmap.org, microsoft.com/24, 192.168.0.1; 10.0.0-255.1-254
      -iL <输入文件名>: 从主机/网络列表输入
      -iR <数目主机>: 选择随机目标
      --exclude <主机1[,主机2][,主机3],...>: 排除 主机/网络
      --excludefile <排除文件>: 从文件排除列表  
    HOST DISCOVERY:
      -sL: 列出扫描 - 简单列出要扫描的目标
      -sn: Ping 扫描 - 禁用端口扫描
      -Pn: 将所有主机视为在线 -- 跳过主机发现
      -PS/PA/PU/PY[端口列表]: TCP SYN/ACK,UDP 或 SCTP 发现到给定端口
      -PE/PP/PM: ICMP 回显,时间戳和网段请求探测
      -PO[协议列表]: IP 协议 Ping
      -n/-R: 从不进行 DNS 解析/始终解析 [默认: 有时]
      --dns-servers <serv1[,serv2],...>: 指定自定义 DNS 服务器
      --system-dns: 使用操作系统的 DNS 解析程序
      --traceroute: 跟踪到每个主机的跃点路径
    SCAN TECHNIQUES:
      -sS/sT/sA/sW/sM: TCP SYN/Connect()/ACK/Window/Maimon 扫描
      -sU: UDP 扫描
      -sN/sF/sX: TCP Null, FIN 和 Xmas 扫描
      --scanflags <标志>: 自定义 TCP 扫描标志
      -sI <僵尸主机[:探测端口]>: 空闲扫描
      -sY/sZ: SCTP INIT/COOKIE-ECHO 扫描
      -sO: IP 协议扫描
      -b <FTP 中继主机>: FTP 反弹扫描
    PORT SPECIFICATION AND SCAN ORDER:
      -p <端口范围>: 仅扫描指定端口
        例如: -p22; -p1-65535; -p U:53,111,137,T:21-25,80,139,8080,S:9
      --exclude-ports <端口范围>: 从扫描中排除指定端口
      -F: 快速模式 - 扫描比默认扫描少的端口
      -r: 顺序扫描端口 - 不随机化
      --top-ports <数目>: 扫描最常见的 <数目> 个端口
      --port-ratio <比例>: 扫描比 <比例> 更常见的端口
    SERVICE/VERSION DETECTION:  
      -sV: 探测开放端口以确定服务/版本信息
      --version-intensity <级别>: 从 0(轻)到 9(尝试所有探测)设置
      --version-light: 限制最可能的探测(强度 2)
      --version-all: 尝试每个探测(强度 9)
      --version-trace: 显示详细的版本扫描活动(用于调试)
    SCRIPT SCAN:
      -sC: 等同于 --script=default
      --script=<Lua 脚本>: <Lua scripts> 是目录、脚本文件或脚本类别的逗号分隔列表
      --script-args=<n1=v1,[n2=v2,...]>: 为脚本提供参数
      --script-args-file=文件名: 在文件中提供 NSE 脚本参数
      --script-trace: 显示发送和接收的所有数据
      --script-updatedb: 更新脚本数据库。
      --script-help=<Lua 脚本>: 关于脚本显示帮助。
               <Lua 脚本> 是脚本文件的逗号分隔列表或脚本类别。
    OS DETECTION: 
      -O: 启用操作系统检测
      --osscan-limit: 将操作系统检测限制为有前途的目标
      --osscan-guess: 更积极地猜测操作系统  
    TIMING AND PERFORMANCE:
      采用 <time> 的选项以秒为单位,或追加 'ms'(毫秒)、's'(秒)、'm'(分钟)或 'h'(小时)到值(例如 30m)。
      -T<0-5>: 设置时间模板(数字越高越快)
      --min-hostgroup/max-hostgroup <大小>: 并行主机扫描组大小 
      --min-parallelism/max-parallelism <numprobes>: 探针并行化
      --min-rtt-timeout/max-rtt-timeout/initial-rtt-timeout <时间>: 指定探针往返时间。
      --max-retries <次数>: 对端口扫描探针重传的次数上限。 
      --host-timeout <时间>: 在此之后放弃目标
      --scan-delay/--max-scan-delay <时间>: 调整探针之间的延迟
      --min-rate <数目>: 发送数据包速率不低于每秒 <数目> 个
      --max-rate <数目>: 发送数据包速率不超过每秒 <数目> 个
    FIREWALL/IDS EVASION AND SPOOFING:
      -f; --mtu <值>: 分片数据包(可选带给定的 MTU)
      -D <诱饵1,诱饵2[,ME],...>: 用诱饵掩饰扫描
      -S <IP 地址>: 伪造源地址
      -e <iface>: 使用指定接口
      -g/--source-port <端口号>: 使用给定的端口号
      --proxies <url1,[url2],...>: 通过 HTTP/SOCKS4 代理转发连接
      --data <十六进制字符串>: 追加自定义有效载荷到发送数据包
      --data-string <字符串>: 追加自定义 ASCII 字符串到发送数据包
      --data-length <数目>: 追加随机数据到发送数据包
      --ip-options <选项>: 用指定的 ip 选项发送数据包
      --ttl <值>: 设置IP时间生存期字段
      --spoof-mac <MAC 地址/前缀/供应商名称>: 伪造你的 MAC 地址
      --badsum: 发送带有错误的 TCP/UDP/SCTP 校验和的数据包
    OUTPUT:
      -oN/-oX/-oS/-oG <文件>: 分别以 normal、XML、s|<rIpt kIddi3 和 Grepable 格式输出扫描结果到给定的文件名。
      -oA <基本名>: 同时以三种主要格式输出
      -v: 增加详细级别(使用 -vv 或更高级获得更大效果)
      -d: 增加调试级别(使用 -dd 或更高级获得更大效果)
      --reason: 显示端口处于特定状态的原因
      --open: 仅显示打开(或可能打开)的端口
      --packet-trace: 显示所有发送和接收的数据包
      --iflist: 打印主机接口和路由(用于调试)
      --append-output: 追加而不是覆盖指定的输出文件
      --resume <文件名>: 恢复一个中止的扫描
      --noninteractive: 禁用通过键盘的运行时交互
      --stylesheet <路径/URL>: XSL 样式表来将 XML 输出转换为 HTML
      --webxml: 引用来自 Nmap.Org 的样式表以获得更可移植的 XML
      --no-stylesheet: 阻止与 XML 输出关联的 XSL 样式表  
    MISC:
      -6: 启用 IPv6 扫描
      -A: 启用操作系统检测,版本检测,脚本扫描和 traceroute
      --datadir <目录名>: 指定自定义 Nmap 数据文件位置
      --send-eth/--send-ip: 使用原始以太网帧或 IP 数据包发送
      --privileged: 假设用户完全有特权
      --unprivileged: 假设用户缺少原始套接字特权
      -V: 打印版本号
      -h: 打印此帮助摘要页面。
    EXAMPLES:
      nmap -v -A scanme.nmap.org
      nmap -v -sn 192.168.0.0/16 10.0.0.0/8
      nmap -v -iR 10000 -Pn -p 80
    SEE THE MAN PAGE (https://nmap.org/book/man.html) FOR MORE OPTIONS AND EXAMPLES
    """)

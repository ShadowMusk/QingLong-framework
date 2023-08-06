def help():
    print("""
    -a <agent_string>       : 指定自定义的USER_AGENT。
    
    -b                       : 使用原始路径。  
    
    -c <cookie_string>       : 为HTTP请求设置cookie。
    
    -E <certificate>         : 客户端证书的路径。
    
    -f                       : 更精细地调整NOT_FOUND(404)检测。
    
    -H <header_string>       : 为HTTP请求添加自定义标头。
    
    -i                       : 使用不区分大小写的搜索。
    
    -l                       : 找到时打印“Location”标头。
    
    -N <nf_code>             : 忽略带有此HTTP代码的响应。
    
    -o <output_file>         : 将输出保存到磁盘。
    
    -p <proxy[:port]>        : 使用此代理。(默认端口是1080)
    
    -P <proxy_username:proxy_password> : 代理身份验证。
    
    -r                       : 不要递归搜索。
    
    -R                       : 交互式递归。(每目录询问一次) 
    
    -S                       : 静默模式。不显示测试过的词。(用于哑终端)
    
    -t                       : 不要在URL上强制结束的'/'。
    
    -u <username:password>   : HTTP身份验证。
    
    -v                       : 也显示NOT_FOUND页面。
    
    -w                       : 不要在警告消息上停止。
    
    -X <extensions> / -x <exts_file> : 在每个词后附加这些扩展名。
    
    -z <millisecs>           : 添加毫秒延迟,以免造成过度洪泛。
    """)

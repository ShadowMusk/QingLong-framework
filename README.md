# 1、QingLong framework ![logo](readme.assets/logo.jpg)

Qinglong is a lightweight Penetration test framework focusing on intranet penetration. Its functions are very powerful and the operation is very simple.

This project will be kept updated for a long time.

# 2、Operating environment

## 2.1 System environment

**All distributions using apt-get, such as**:

- Ubuntu and its derivatives such as Linux Mint,Elementary OS,etc
- Debian
- Kali Linux

**All distributions using yum, such as**:

- Red Hat Enterprise Linux(RHEL)
- Fedora
- CentOS
- Scientific Linux

## 2.2 Python version

The Python version should not be lower than **3.6** (this project is developed based on Python 3.6, and perhaps other Python versions lower than 3.6 can also run this project)

# 3、Functional module          

Qinglong currently has six major functional modules, namely **information collection module**, **vulnerability scanning module**, **password cracking module**, **malicious attack module**, **denial of service attack module**, and **internal network penetration module**.

**Information collection module**: (1) query whois information, Subdomain, segment C, IP information, website filing (2) judge whether there is a CDN (3) WAF identification (4) directory scanning (5) nmap scanning

**Vulnerability scanning module**: integrating three major vulnerability scanning tools: sqlmap, nikto, and wapiti.

**Password cracking module**: integrating four major password cracking tools: Hydra, Medusa, Hashcat, and John.

**Malicious attack module**: email phishing and email bombing.

**Denial of service attack modules**: hping3, slowloris, goldeneye, hammer, DDos Attack.

**Intranet penetration module**: backdoor generation, backdoor monitoring, multi backdoor connection, domain information collection, privilege promotion, privilege maintenance, domain horizontal movement attack, domain controller security, Mimikatz, Tunnel broker.

# 4、Tutorial

### （1）Launch framework

Firstly, go to the directory of the framework:

```shell
cd QingLong-framework
```

Next, run the following command to install the required dependencies for the framework:                         

```shell
python3 dependencies.py
```

Then, run the following command to start the framework:

```shell
python3 index.py
```

### （2）How to use it

When tapping the tab key, the command bar will display optional commands. Select "let's start" to enter the framework.

For more detailed usage steps, please refer to the link:[ShadowMusk/QingLong-Using-Tutorials: Ways to use QingLong framework (github.com)](https://github.com/ShadowMusk/QingLong-Using-Tutorials)

# 5、Disclaimers

This Penetration test tool is only used for authorized Penetration test and safety assessment activities!

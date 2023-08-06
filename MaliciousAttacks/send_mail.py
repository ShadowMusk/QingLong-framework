import smtplib
from email.mime.text import MIMEText
from email.utils import formataddr


def send_mail(server_mail_addr, port, from_addr, password, to_addr, template_path, subject):
    try:
        smtp = smtplib.SMTP_SSL(server_mail_addr, port=int(port))
        smtp.login(user=from_addr, password=password)
        with open(template_path, "r", encoding="utf-8") as f:
            file_content = f.read()
        message = MIMEText(file_content, "html", "utf-8")
        message["From"] = formataddr(["fairly", from_addr])
        message["To"] = formataddr(["jack", to_addr])
        message["Subject"] = subject
        smtp.sendmail(from_addr=from_addr, to_addrs=to_addr, msg=message.as_string())
        smtp.quit()
        print('\033[1;32;32m' + "[+] Successfully sent email!" + '\033[0m')
    except:
        print('\033[1;31;31m' + "[-] Sending failed! Please check if all parameters are correct." + '\033[0m')

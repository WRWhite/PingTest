# References
# https://medium.com/@DevOpsNuts/python-ping-an-ip-adress-663ed902e051#:~:text=the%20successful%20ping.-,We%20use%20%E2%80%9CPopen%E2%80%9D%20and%20%E2%80%9CPIPE%E2%80%9D,functions%20from%20the%20subprocess%20module.&text=Then%2C%20we%20create%20a%20function,def%20ping%20(host%2Cping_count)%3A
# https://myadventuresincoding.wordpress.com/2024/09/14/python-how-to-send-an-email-with-an-attachment/
# https://docs.python.org/3/library/email.mime.html
# https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp
# https://www.w3schools.com/python/python_file_open.asp


# Modules for ping() function
from re import findall
from subprocess import Popen, PIPE

# Modules for send_mail() function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# General modules
from datetime import date
from os import path, remove

def ping (host: list, ping_count: int) -> str:

    results_file = open('ping-test-results.txt','w')
    email_file = open('email-msg.txt','w')

    sucess_cnt: int = 0
    fail_cnt: int = 0
    for ip in host:
        data: str = ""
        output: str = Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test: list = findall("TTL", data)

        if ping_test:
            print(f"{ip} \t {host[ip]} \t : Successful Ping", file=results_file)
            print(f"{ip} \t {host[ip]} \t : Successful Ping")
            sucess_cnt +=1
        else:
            print(f"{ip} \t {host[ip]} \t : Failed Ping", file=results_file)
            print(f"{ip} \t {host[ip]} \t : Failed Ping")
            fail_cnt +=1

    print(f"{fail_cnt} out of {sucess_cnt+fail_cnt} hosts failed to respond to ping", file=email_file )

    results_file.close()
    email_file.close()


    if fail_cnt > 0: 
        return " !!! ***** <PING TEST FAILED> <PING TEST FAILED> <PING TEST FAILED> ***** !!!"
    else:
        return " pass"


def send_email(subject: str, body: str, sender: str, recipients: str, password: str,) -> None:
    msg: str = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    attachment_filename :str  = "ping-test-results.txt"
    msg.attach(MIMEText(body, 'plain'))
    if attachment_filename:
        attachment = open(attachment_filename, 'rb')
        part: MIMEBase = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_filename}")
        msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")
    attachment.close()



def main():

    today: date = date.today()

    nodes: dict = {
         "192.168.16.10" : "CRM-WW            ",
         "192.168.16.11" : "CRM-NG            ", 
         "192.168.16.12" : "CRM-SP            ",
         "192.168.16.13" : "CRM-DP            ",
         "192.168.16.14" : "CRM-BK            ",
         "192.168.16.20" : "WiFi-Node1        ", 
         "192.168.16.21" : "WiFi-Node2        ", 
         "192.168.16.31" : "WS21-Scanne       ", 
         "192.168.16.32" : "WS23-Win7-Suppoer ",   
         "192.168.16.34" : "WS27-DavidLangford", 
         "192.168.16.35" : "WS28-William      ",
         "192.168.16.50" : "Phone-PolyCom1    ",
         "192.168.16.51" : "Phone-PolyCom2    ",
         "192.168.16.52" : "Phone-PolyCom3    ", 
         "192.168.16.53" : "Phone-PolyCom4    ",
         "192.168.16.54" : "Phone-PolyCom5    ", 
         "192.168.16.55" : "Phone-PolyCom6    ", 
         "192.168.16.58" : "DI-HOST           ", 
         "192.168.16.59" : "DINAS             ", 
         "192.168.16.60" : "DI-HOST2          "
         }


    # If previous email files exist remove them
    if path.exists("email-msg.txt"):
        remove("email-msg.txt")
    if path.exists("ping-test-results.txt"):
        remove("ping-test-results.txt")

    # Generate ping results
    status :str = ping(nodes,3)

    # Email ping results
    email_file = open('email-msg.txt','r')
    body: str = email_file.read()
    email_file.close()
    subject: str = f"Ping Test {today} {status}"
    sender: str = "william.white.directinsight@googlemail.com"
    #recipients: str = ["william.white@directinsight.co.uk"]
    recipients: str = ["william.white@directinsight.co.uk", "nigel.goodyear@directinsight.co.uk", "support@directinsight.co.uk"]
    # Gmail application password:
    password: str = "qwekflvtxxzwmwsg"

    send_email(subject, body, sender, recipients, password)



if __name__ == "__main__":
    main()






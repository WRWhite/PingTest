# https://medium.com/@DevOpsNuts/python-ping-an-ip-adress-663ed902e051#:~:text=the%20successful%20ping.-,We%20use%20%E2%80%9CPopen%E2%80%9D%20and%20%E2%80%9CPIPE%E2%80%9D,functions%20from%20the%20subprocess%20module.&text=Then%2C%20we%20create%20a%20function,def%20ping%20(host%2Cping_count)%3A

# https://myadventuresincoding.wordpress.com/2024/09/14/python-how-to-send-an-email-with-an-attachment/

# https://docs.python.org/3/library/email.mime.html

# https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp

# https://www.w3schools.com/python/python_file_open.asp


# For ping() function
from re import findall
from subprocess import Popen, PIPE

# For send_mail() function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from datetime import date


def ping (host,ping_count):

    results_file = open('ping-test-results.txt','w')
    email_file = open('email-msg.txt','w')

    sucess = 0
    fail = 0
    for ip in host:
        data = ""
        output= Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{ip} \t {host[ip]} \t\t : Successful Ping", file=results_file)
            print(f"{ip} \t {host[ip]} \t\t : Successful Ping")
            sucess +=1
        else:
            print(f"{ip} \t {host[ip]} \t\t : Failed Ping", file=results_file)
            print(f"{ip} \t {host[ip]} \t\t : Failed Ping")
            fail +=1

    print(f"{fail} out of {sucess+fail} hosts failed to respond to ping", file=email_file )

    if fail > 0: 
        return " ***** <PING TEST FAILED> <PING TEST FAILED> <PING TEST FAILED> *****"
    else:
        return " pass"



nodes = {"192.168.16.10" : "CRM-WW",
         "192.168.16.11" : "CRM-NG", 
         "192.168.16.12" : "CRM-SP",
         "192.168.16.13" : "CRM-DP",
         "192.168.16.14" : "CRM-BK",
         "192.168.16.20" : "WiFi-Node1", 
         "192.168.16.21" : "WiFi-Node2", 
         "192.168.16.31" : "WS21-Scanner", 
         "192.168.16.32" : "WS23-Win7-Suppoer",   
         "192.168.16.34" : "WS27-DavidLangford", 
         "192.168.16.35" : "WS28-William",
         "192.168.16.51" : "Phone-PolyCom2",
         "192.168.16.52" : "Phone-PolyCom3", 
         "192.168.16.53" : "Phone-PolyCom4",
         "192.168.16.54" : "Phone-PolyCom5", 
         "192.168.16.55" : "Phone-PolyCom6", 
         "192.168.16.58" : "DI-HOST", 
         "192.168.16.59" : "DINAS", 
         "192.168.16.60" : "DI-HOST2"}

def send_email(subject, body, sender, recipients, password,):
    msg = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    attachment_filename = "ping-test-results.txt"
    msg.attach(MIMEText(body, 'plain'))
    if attachment_filename:
        attachment = open(attachment_filename, 'rb')
        part = MIMEBase('application', 'octet-stream')
        part.set_payload(attachment.read())
        encoders.encode_base64(part)
        part.add_header('Content-Disposition', f"attachment; filename= {attachment_filename}")
        msg.attach(part)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")



def main():

    today = date.today()

    # Generate ping results
    status = ping(nodes,3)

    # Email ping results

    email_file = open('email-msg.txt','r')
    body = email_file.read()
    subject = f"Ping Test {today} {status}"
    sender = "william.white.directinsight@googlemail.com"
    recipients = ["william.white@directinsight.co.uk", "nigel.goodyear@directinsight.co.uk", "support@directinsight.co.uk"]
    # Gmail application password:
    password = "qwekflvtxxzwmwsg"

    send_email(subject, body, sender, recipients, password)


if __name__ == "__main__":
    main()






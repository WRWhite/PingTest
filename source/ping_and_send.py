# References
# https://medium.com/@DevOpsNuts/python-ping-an-ip-adress-663ed902e051#:~:text=the%20successful%20ping.-,We%20use%20%E2%80%9CPopen%E2%80%9D%20and%20%E2%80%9CPIPE%E2%80%9D,functions%20from%20the%20subprocess%20module.&text=Then%2C%20we%20create%20a%20function,def%20ping%20(host%2Cping_count)%3A
# https://myadventuresincoding.wordpress.com/2024/09/14/python-how-to-send-an-email-with-an-attachment/
# https://docs.python.org/3/library/email.mime.html
# https://stackoverflow.com/questions/64505/sending-mail-from-python-using-smtp
# https://www.w3schools.com/python/python_file_open.asp


# Modules for ping() function
from re import findall
from subprocess import Popen, PIPE
from csv import reader

# Modules for send_mail() function
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

# General modules
from datetime import datetime, date
from os import path, remove

def ping (host: list[str], ping_count: int) -> str:

    # CSV format:
    results_file = open('ping-test-results.csv','w')
    # Plain text format:
    #results_file = open('ping-test-results.txt','w')
    email_file = open('email-msg.txt','w')
    #timestamp: datetime = date.today()
    timestamp: datetime = datetime.now()

    sucess_cnt: int = 0
    fail_cnt: int = 0
    # CSV column headings:
    print(f"IP Address,,Host Name,,,Status", file=results_file)
    print(f",,", file=results_file)
    for ip in host:
        data: str = ""
        output: str = Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test: list = findall("TTL", data)

        if ping_test:
            # Plain text output:
            #print(f"{ip} \t {host[ip]} \t : Successful Ping", file=results_file)
            print(f"{ip},,{host[ip]},,,sucess", file=results_file)
            # CSV Output
            print(f"{ip} \t {host[ip]} \t : Successful Ping")
            sucess_cnt +=1
        else:
            # Plain text output:
            #print(f"{ip} \t {host[ip]} \t : Failed Ping", file=results_file)
            print(f"{ip},,{host[ip]},,,failed", file=results_file)
            # CSV Output:
            print(f"{ip} \t {host[ip]} \t : Failed Ping")
            fail_cnt +=1

    print(f"\nTimestamp: {timestamp}", file=results_file)
    print(f"{fail_cnt} out of {sucess_cnt+fail_cnt} hosts failed to respond to ping", file=email_file )
    print(f"Timestamp: {timestamp}", file=email_file)

    results_file.close()
    email_file.close()

    if fail_cnt > 0: 
        return (" ! <PING TEST FAILED> <PING TEST FAILED> <PING TEST FAILED> !")
    else:
        return (" pass")


def send_email(subject: str, body: str, sender: str, recipients: str, password: str,) -> None:

    msg: str = MIMEMultipart()
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

    # CSV test format:
    attachment_filename :str  = "ping-test-results.csv"
    # Plain text format:
    #attachment_filename :str  = "ping-test-results.txt"

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
    
    # Read in a CSV file containing the IP/Host_Name as a key value pair in a dictionary
    if path.exists("host_data.csv"):
        with open('host_data.csv', 'r') as csv_file:
            csv_reader = reader(csv_file)
            nodes = {rows[0]: rows[1] for rows in csv_reader}
             #print(nodes
    else:
        print("ERROR:- Input file 'host_data.csv' does not exist")
        return -1

    # The above code reads in a dictionary of the form
#    nodes: dict[str,str] = {
#         "192.168.16.10" : "CRM-WW             ",
#         "192.168.16.11" : "CRM-NG             ", 
#         "192.168.16.60" : "DI-HOST2           ",
#         "8.8.8.8      " : "Internet           "
#         }

    # If previous email files exist remove them
    if path.exists("email-msg.txt"):
        remove("email-msg.txt")
    if path.exists("ping-test-results.txt"):
        remove("ping-test-results.txt")
    if path.exists("ping-test-results.csv"):
        remove("ping-test-results.csv")

    # Generate ping results
    status :str = ping(nodes,3)

    # Email ping results
    # timestamp: date = date.today()
    timestamp: datetime = datetime.now()
    email_file = open('email-msg.txt','r')
    body: str = email_file.read()
    email_file.close()
    subject: str = f"Ping Test {status} {timestamp} "
    sender: str = "william.white.directinsight@googlemail.com"
    recipients: str = ["william.white@directinsight.co.uk"]
    #recipients: str = ["william.white@directinsight.co.uk", "nigel.goodyear@directinsight.co.uk", "support@directinsight.co.uk"]
    # Gmail application password:
    password: str = "qwekflvtxxzwmwsg"

    send_email(subject, body, sender, recipients, password)

    # Delete *email_file* but not the *results_file*
    if path.exists("email-msg.txt"):
        remove("email-msg.txt")
    #if path.exists("ping-test-results.txt"):
    #    remove("ping-test-results.txt")
    #if path.exists("ping-test-results.csv"):
    #    remove("ping-test-results.csv")
    


if __name__ == "__main__":
    main()






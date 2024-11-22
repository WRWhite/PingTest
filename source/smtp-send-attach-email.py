import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders

from datetime import date

email_file = open('email-msg.txt','r')

today = date.today()

subject = f"Ping Test {today}"
#body = "This is the body of the text message"
body = email_file.read()
sender = "william.white.directinsight@googlemail.com"
#recipients = ["william.white@directinsight.co.uk", "support@directinsight.co.uk"]
recipients = ["william.white@directinsight.co.uk"]
password = "qwekflvtxxzwmwsg"

attachment_filename = "ping-test-results.txt"


def send_email(subject, body, sender, recipients, password,):
    msg = MIMEMultipart()
    #msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)

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


send_email(subject, body, sender, recipients, password)
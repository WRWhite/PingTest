import smtplib
from email.mime.text import MIMEText
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



def send_email(subject, body, sender, recipients, password,):
    msg = MIMEText(body)
    msg['Subject'] = subject
    msg['From'] = sender
    msg['To'] = ', '.join(recipients)
    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp_server:
       smtp_server.login(sender, password)
       smtp_server.sendmail(sender, recipients, msg.as_string())
    print("Message sent!")


send_email(subject, body, sender, recipients, password)
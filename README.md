# PingTest
Ping Tester Application - ping_and_send.py  
PingTest is written in Python3 (3.11.4) so it will run on Windows or Linux. Below are the instructions for installing under Windows.  
Currently it noly works with Gmail SMTP.  

# Installation for MS Windows / Windows Server  
Create a directory on the host machine to contain PingTester eg C:\PING-TEST.   
copy ping_amd_send.py into this directory.  
copy the host_data.csv file into the same directory.    
Create a file called smpt-config.txt file in the same directory.  
Edit the host_data.csv file and modify as required, the format is: 

```
ip-address,host-name 
```
Edit the smpt-config.txt and add your Gmail smtp credentials, the format is as follows  
(blank lines and lines beginning with a "#" are ignored).  
The chevrons "<" and ">" should be omitted:  

```
# User name / from address:
<user_name@googlemail.com>

# Gmail application password:
<gmail_application_password>
```

PingTest will creat a log file containing the results of the "ping" on each host in the host_data.csv file. This file is then automatically emailed as an attachment to the email list in a file passed as a command line argument, one email per line eg:   

```
python ping_and_send.py email-list.txt
```

If the  email-list.txt file is not provided, ping_and_send.py will still run but no emails will be sent.  

Create a Windows task in Task Scheduler to run the task daily at a convenient time. Alternatively simply inport the   
"Win10-Task-Scheduler_PingTest.xml" file into Windows Task Scheduler.  

# PingTest
Ping Tester Application - ping_and_send.py  
PingTest is written in Python3 so it will run on Windows or Linux. Below are the instructions for installing under Windows.  


# Installation for MS Windows / Windows Server  
Create a directory on the host machine to contain PingTester eg C:\PING-TEST.   
copy ping_amd_send.py into this directory.  
copy the host_data.csv file into the same directory.    
Edit the host_data file and modify as required, the format is: 

```
ip-address,host-name 
```

PingTest will creat a log file containing the results of the "ping" on each host in the host_data.csv file. This file is then automatically emailed as an attachment to the email list in a file called email-list.txt, one email per line. This file can be passed as a command line arguement to ping_amd_send.py eg:   

```
python ping_and_send.py email-list
```

If the  email-list.txt file is not provide, ping_and_send.py will use the hard coded default.  

Create a Windows task in Task Scheduler to run the task daily at a convenient time. Alternatively simply inport the   
"Win10-Task-Scheduler_PingTest.xml" file into Windows Task Scheduler.  





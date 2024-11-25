# PingTest
Ping Tester Application - ping_and_send.py  
PingTest is written in Python3 so it will run on Windows or Linux. Below are the instructions for installing under Windows.  


# Installation for MS Windows / Windows Server  
Create a directory on the host machine to contain PingTester eg C:\PING-TEST.   
copy ping_amd_send.py into this directory.  
copy the host_data_csv file into the same directory.    
Edit the host_data file and modify as required, the format is:  
ip-address,host-name  
The email "recipients" variable is hard coded. Modily as necessary (search for "# Email ping results").  
Create a Windows task in Task Scheduler to run the task daily at a convenient time. Alternatively simply inport the   
"Win10-Task-Scheduler_PingTest.xml" file into Windows Task Scheduler.  





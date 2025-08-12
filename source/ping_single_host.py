# https://stackoverflow.com/questions/2953462/pinging-servers-in-python

import os, time, datetime
#param = '-n' if os.sys.platform().lower()=='win32' else '-c'
hostname = "google.com" # Host to be pinged
delay = 10 # Delay between pings
pingResultsFile = 'pingResults.txt'

# Open and time stamp results file
resultsFile = open(pingResultsFile,'a')
resultsFile.write(f"Test session opened at {datetime.datetime.now()}\n\n")
resultsFile.close()

while True:
   response = os.system(f"ping -n 1 {hostname}")
   print(datetime.datetime.now())
   if response == 1: # 0 == ping sucess, 1 == ping failed
   # If no reply from hostname add a time stamp to the file with a note
        #print(f"{hostname} is down!")
        resultsFile = open(pingResultsFile,'a')
        #now = datetime.datetime.now()
        resultsFile.write(f"{datetime.datetime.now()} {hostname} cannot be reached!\n")
        resultsFile.close()
   time.sleep(delay) 




# https://stackoverflow.com/questions/2953462/pinging-servers-in-python

import os, time, datetime
#param = '-n' if os.sys.platform().lower()=='win32' else '-c'
hostname = "google.com" # Host to be pinged
longDelay = 60  # Delay between sucesfull pings. 
ShortDelay = 20 # Delay between failed pings 
lastPingStatus = 1 # 1 == last ping failed, 0 == last ping passed
pingResultsFile = 'pingResults.txt'

# Open and time stamp results file
resultsFile = open(pingResultsFile,'a')
resultsFile.write(f"\nTest session opened at {datetime.datetime.now()}\n")
resultsFile.close()

while True:
   response = os.system(f"ping -n 1 {hostname}")
   print(datetime.datetime.now()) # Write ping timestamp to
   if response == 1: # 0 == ping sucess, 1 == ping failed
   # If ping fails add a time stamp to the file with a note
        delay = ShortDelay  
        resultsFile = open(pingResultsFile,'a')
        if lastPingStatus == 0:
            resultsFile.write("\n")
        resultsFile.write(f"{datetime.datetime.now()} {hostname} cannot be reached!\n")
        resultsFile.close()
        lastPingStatus = 1
   else:
       delay = longDelay
       lastPingStatus = 0
   time.sleep(delay) 

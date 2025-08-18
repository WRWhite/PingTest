# https://stackoverflow.com/questions/2953462/pinging-servers-in-python

import os, time, datetime

HOST_NAME = "google.com" # Host to be pinged
LONG_DELAY = 60  # Delay between sucesfull pings
SHORT_DELAY = 20 # Delay between failed pings 
PING_SUCESS = 0
PING_FAIL = 1
PING_RESULTS_FILE = 'pingResults.txt'

lastPingStatus = PING_FAIL

# Open and time stamp results file
resultsFile = open(PING_RESULTS_FILE,'a')
resultsFile.write(f"\nTest session opened at {datetime.datetime.now()}\n")
resultsFile.close()

while True:
   PingResponse = os.system(f"ping -n 1 {HOST_NAME}")
   print(datetime.datetime.now()) # Write ping timestamp to
   if PingResponse == PING_FAIL: 
   # If ping fails add a time stamp to the file with a note
   # and switch to a finer delay resolution
        resultsFile = open(PING_RESULTS_FILE,'a')
        delay = SHORT_DELAY  
        if lastPingStatus == PING_SUCESS: # Add a line in results file to indicate end of current failure
            resultsFile.write("\n")
        resultsFile.write(f"{datetime.datetime.now()} {HOST_NAME} cannot be reached!\n")
        resultsFile.close()
        lastPingStatus = PING_FAIL
   else:
       delay = LONG_DELAY
       lastPingStatus = PING_SUCESS
   time.sleep(delay) 




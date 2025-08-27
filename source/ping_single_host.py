# https://stackoverflow.com/questions/2953462/pinging-servers-in-python

import os, time, datetime

HOST_NAME = "google.com" # Host to be pinged
LONG_DELAY = 3  # Delay between sucesfull pings (default = 60)
SHORT_DELAY = 1 # Delay between failed pings (default = 15)
PING_SUCESS = 0 
PING_FAIL = 1
RESULTS_FILE = 'pingResults.txt'

# Open and time stamp results file
with open(RESULTS_FILE,'a') as results_file:
    results_file.write(f"\nTest session opened at {datetime.datetime.now()}\n")

last_ping_status = PING_FAIL
while True:
   ping_response = os.system(f"ping -n 1 {HOST_NAME}")
   print(datetime.datetime.now()) # Write ping timestamp to
   if ping_response == PING_FAIL: 
   # If ping fails add a time stamp to the file with a note
   # and switch to a finer delay resolution
        delay = SHORT_DELAY
        with open(RESULTS_FILE,'a') as results_file:
            if last_ping_status == PING_SUCESS: # Add a line in results file to indicate end of current failure
                results_file.write("\n")
            results_file.write(f"{datetime.datetime.now()} {HOST_NAME} cannot be reached!\n")
        last_ping_status = PING_FAIL
   else:
       delay = LONG_DELAY
       last_ping_status = PING_SUCESS
   time.sleep(delay) 




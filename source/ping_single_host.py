# https://stackoverflow.com/questions/2953462/pinging-servers-in-python

import os, time, datetime
from typing import TextIO

def main() -> None:

    LONG_DELAY: int = 6  # Delay between sucesfull pings (default = 60)
    SHORT_DELAY: int = 1 # Delay between failed pings (default = 10)
    PING_SUCESS: int = 0 
    PING_FAIL: int = 1
    RESULTS_FILE: str = 'pingResults.txt'

    ping_response: int = PING_FAIL
    last_ping_status: int = PING_FAIL
    delay: int = LONG_DELAY
    results_file: TextIO # Text file object or "handle"

    # Time stamp results file with test start time
    with open(RESULTS_FILE,'a') as results_file:
        results_file.write(f"\nTest session started at {datetime.datetime.now()}\n")

    while True:
        ping_response = ping_test("google.com", "aws.com")
        if ping_response != PING_SUCESS: 
        # If ping fails switch to a finer delay resolution
            delay = SHORT_DELAY
            with open(RESULTS_FILE,'a') as results_file:
                if last_ping_status == PING_SUCESS: # Add a line in results file to indicate end of current failure
                    results_file.write("\n")
                results_file.write(f"{datetime.datetime.now()} hosts cannot be reached!\n")
            last_ping_status = PING_FAIL
        else:
            delay = LONG_DELAY
            last_ping_status = PING_SUCESS
        time.sleep(delay) 


def ping_test(host1: str, host2: str) -> int:

    PING_SUCESS = 0
    PING_FAIL = 1
    ping_response: int = PING_SUCESS
    ping_response_host1: int = PING_SUCESS
    ping_response_host2: int = PING_SUCESS

    ping_response_host1 = os.system(f"ping -n 3 {host1}")
    print(datetime.datetime.now()) # Write ping timestamp to console
    ping_response_host2 = os.system(f"ping -n 3 {host2}")
    print(datetime.datetime.now()) # Write ping timestamp to console

    if (ping_response_host1 != PING_SUCESS) and (ping_response_host2 != PING_SUCESS):
        ping_response = PING_FAIL
    else:
        ping_response = PING_SUCESS    
       
    return ping_response


if __name__ == "__main__":
    main()




from re import findall
from subprocess import Popen, PIPE

def ping (host,ping_count):

    for ip in host:
        data = ""
        output= Popen(f"ping {ip} -n {ping_count}", stdout=PIPE, encoding="utf-8")

        for line in output.stdout:
            data = data + line
            ping_test = findall("TTL", data)

        if ping_test:
            print(f"{ip} : Successful Ping")
        else:
            print(f"{ip} : Failed Ping")

#nodes = ["8.8.8.8", "20.20.20.50", "facebook.com", "192.168.1.20"]
nodes = ["192.168.16.10", "192.168.16.11", "192.168.16.12", "192.168.16.13" ]

ping(nodes,3)
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

nodes = ["192.168.16.10", "192.168.16.11", "192.168.16.12", "192.168.16.13", "192.168.16.20", "192.168.16.21", 
         "192.168.16.31", "192.168.16.34", "192.168.16.35", "192.168.16.51", "192.168.16.52", "192.168.16.53",
         "192.168.16.54", "192.168.16.55", "192.168.16.58", "192.168.16.59", "192.168.16.60"]

ping(nodes,3)

import socket 
import time

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
local_hostname = socket.gethostname()
local_fqdn = socket.getfqdn()
ip_address = socket.gethostbyname(local_hostname)

server_address = (ip_address, 23456)
sock.connect(server_address)

print("connection to %s (%s) with %s" %(local_hostname, local_fqdn, ip_address))

temperature_data = ['15','33','44','12','11','26']

for entry in temperature_data:
    print("data: %s" %entry)
    new_data = str("temp: %s\n" %entry).encode("utf-8")
    sock.sendall(new_data)
    time.sleep(2)

sock.close()    
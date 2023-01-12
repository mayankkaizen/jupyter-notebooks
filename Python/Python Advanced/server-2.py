

from socket import *
from fib import fib 
from threading import Thread

def fib_server(address):
    sock = socket(AF_INET, SOCK_STREAM) #(1st param: address family, 2nd param: socket type)
    sock.setsockopt(SOL_SOCKET, SO_REUSEADDR,1) #(lev,opt,value)see comment 'a' in end of code for understanding params
    sock.bind(address)
    sock.listen(5)  #'5' number of unaccepted connections the system will allow before refusing new connections.
    while True:
        client,addr = sock.accept() #accept a connection. Returns (conn,addr), conn is new socket obj for data exchange
        print("Connection", addr)
        Thread(target=fib_handler, args=(client,)).start() 
        
def fib_handler(client):
    while True:
        req = client.recv(128)  # waits for data that sent by the client.
        if not req: break
        result = fib(int(req))
        resp = str(result).encode('ascii') + b'\n'
        client.send(resp) # sends data back to the client.
        print(resp)
    print("Closed")
    
fib_server(('', 25000))

#'a' -  refer this https://pubs.opengroup.org/onlinepubs/7908799/xns/getsockopt.html 
# setsockopt params means search SO_REUSEADDR on the socket level (SOL_SOCKET)itself and set it to 1

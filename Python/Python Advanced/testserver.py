
from socket import *

sock = socket(AF_INET, SOCK_STREAM)
sock.bind(('localhost',11000))
print(sock.getsockname())
sock.listen(2)

while True:
    conn, addr = sock.accept()
    print("connected to: ", addr)
    while True:
        msg = conn.recv(1024)
        print("received msg: ", msg)
        if msg:
            conn.sendall(msg)
            print('msg sent: ', msg)
        else:
            sock.close()
            break
            

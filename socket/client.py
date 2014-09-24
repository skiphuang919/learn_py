#!/usr/bin/env python
from socket import *

HOST='127.0.0.1'
PORT=8889
BUFSIZE=1024
ADDR=(HOST,PORT)

tcpCliSock=socket(AF_INET,SOCK_STREAM)
tcpCliSock.connect(ADDR)
print tcpCliSock.recv(BUFSIZE)
while True:
    data=raw_input('>')
    if not data:
        break
    tcpCliSock.send(data)
    data=tcpCliSock.recv(BUFSIZE)
    if not data:
        break
    print data

tcpCliSock.close()

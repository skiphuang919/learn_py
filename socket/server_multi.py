#!/usr/bin/env python
from socket import *
import threading
HOST='127.0.0.1'
PORT=8889
BUFSIZE=1024
ADDR=(HOST,PORT)

def con():
    new_sock.send('welcome!')
    print 'connect successful from %s:%s' % addr
    while True:
        data=new_sock.recv(BUFSIZE)
        if not data:
            break
        new_sock.send('hello %s'%data)
    new_sock.close()
    print 'Connection from %s:%s closed.' % addr

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
print 'waiting for connection....'
while True:
    new_sock,addr=tcpSerSock.accept()
    t=threading.Thread(target=con)
    t.start()


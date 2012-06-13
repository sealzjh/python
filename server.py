#!/usr/bin/python
#server
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM);

host = '127.0.0.1'
port = 5001
s.bind((host , port))
s.listen(10)

while True:
    c, addr = s.accept();
    print 'Get connection from',addr
    c.send('This is a simple server')
    c.close();

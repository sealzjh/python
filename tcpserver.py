#!/usr/bin/python
#tcp server
from SocketServer import TCPServer , StreamRequestHandler
class MyHandler(StreamRequestHandler):
    def handle(self):
        addr = self.request.getpeername()
        print "Get connection from ",addr
        self.wfile.write('This is a tcp socket server')

host = '127.0.0.1'
port = 2234
server = TCPServer((host , port) , MyHandler)
server.serve_forever()
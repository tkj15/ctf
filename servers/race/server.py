#!/usr/bin/python
# -*- coding: utf-8 -*-

import SocketServer, subprocess

class ClientHandler(SocketServer.BaseRequestHandler):

     def handle(self):
         fd = self.request.fileno()
         #cmd = '/usr/bin/python','/vagrant/servers/race/handler.py -u'
         subprocess.Popen(['/usr/bin/python','/vagrant/servers/race/handler.py'], stdin=fd, stdout=fd, stderr=fd).communicate()

if __name__ == "__main__":
     #for fbctf: 10.10.10.5; for picoctf:0.0.0.0
     HOST, PORT = "0.0.0.0", 19999
     SocketServer.ThreadingTCPServer.allow_reuse_address = True
     server = SocketServer.ThreadingTCPServer((HOST, PORT), ClientHandler)
     server.serve_forever()



#!/usr/bin/python

import SocketServer
# SocketServer framework for network servers

class EchoHandler(SocketServer.BaseRequestHandler):


    #The request handler class for our server.It is instantiated once per connection to the server, and must
    #override the handle() method to implement communication to the client.


	def handle(self):

		print "Got Connection from:", self.client_address
		data = 'dummy' 
		
		while len(data):
			data = self.request.recv(1024)
                # self.request is the TCP socket connected to the client
			print "Client sent: " + data
			self.request.send(data)
		print "Client Left"

serverAddr = ("0.0.0.0", 9999)

#create a TCP Server
server = SocketServer.TCPServer(serverAddr, EchoHandler)

server.serve_forever()

# Activate the server; this will keep running until someone interrupt the program with Ctrl-C

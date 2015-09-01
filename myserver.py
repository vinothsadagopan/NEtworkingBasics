from os import curdir, sep 
import os.path
import argparse
from BaseHTTPServer import HTTPServer, BaseHTTPRequestHandler
from SocketServer import ThreadingMixIn
import threading
import socket
parser = argparse.ArgumentParser(description='Enter your input') 
parser.add_argument("port" , help="Enter port") #Getting the port number as input
args = parser.parse_args()
port_number = int(args.port) #coverting port number to integer
class MyHandler(BaseHTTPRequestHandler):
	def do_GET(self): #implementing get part of http server
		try:
			f = open(curdir + sep + self.path, 'r') #opening the given file in read mode
			self.send_response(200) #sending a response of 200 back to client once the file has been read
			self.send_header('Content-type','text/html')
			self.end_headers()
			self.wfile.write(f.read()) #Contains the output stream for writing a response back to the client.
			f.close()
			return
		except IOError:
			self.send_error(404,'File Not Found') #error message if file is not found
	
	def do_PUT(self):
		try:
			length = int(self.headers['Content-Length']) #finding the length of the contents to be written
			file = self.rfile.read(length)
   			location = 'E:/' 
   			newpath = os.path.join(location , self.path.decode('string_escape')) #indication the location along with file name to be created
   			file1 = open(newpath,'w') #creates a new file with content name
   			file1.write(file) #writes file contents to new file
			self.send_response(200,'File created in the location specified') #send acknowledgement
			file1.close()
            
		except IOError:
			self.send_error('Unable to transfer file')
			
class ThreadedHTTPServer(ThreadingMixIn , HTTPServer): 
	""" Creating a multithreaded HTTPServer  which creates a new thread for handling new requests"""

if __name__ == '__main__':
	try:
		value=('127.0.0.1',port_number)
		server = ThreadedHTTPServer(value,MyHandler)
		print "Server Started"
		print 'ctrl z to stop on mac and ctrl c to stop on windows'
		server.serve_forever()
	except KeyboardInterrupt:
		print 'ctrl z to close on mac or ctrl c to close on windows'
		server.socket.close()
    
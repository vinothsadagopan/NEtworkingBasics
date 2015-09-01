import argparse
import httplib

parser = argparse.ArgumentParser(description='getting input parameters')
parser.add_argument("hostname" , help= "Input your hostname")                               
parser.add_argument("port" , help= "Enter port_number?")
parser.add_argument("command" , help= "enter either GET or PUT?")
parser.add_argument("filename" , help= "Enter filename to transfer or retrieve")
args = parser.parse_args()


if args.command.upper() == 'GET':
	connection = httplib.HTTPConnection(args.hostname,args.port)
	connection.request("GET","/"+args.filename)
	response = connection.getresponse()
	print response.status, response.reason
	retrievedfile = response.read()
	print retrievedfile
	connection.close()

elif args.command.upper() == 'PUT':
	file = open(args.filename, 'r')
	connection = httplib.HTTPConnection(args.hostname,args.port)
	connection.request("PUT", "/" + args.filename , file.read())
	response = connection.getresponse()
	print response.status, response.reason
	connection.close()
else:
	print 'Invalid '+  args.command + ' command.Only GET and PUT can be entered'
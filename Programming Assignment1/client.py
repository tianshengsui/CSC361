#import socket module
from socket import *
import sys # In order to terminate the program

try:
    #create an AF_INET, STREAM socket4
    s = socket(AF_INET, SOCK_STREAM)
except socket.error, msg:
    print("Failed to create socket. Error code: "+str(msg[0]) + ", Error message : "+msg[1])
    sys.exit()
print("Socket Created")

IP_address = sys.argv[1]
port_number = sys.argv[2]
file_name = sys.argv[3]

s.connect((IP_address, int(port_number)))
print("Socket connected to " + IP_address + "on Port " + port_number)

request = "GET /" + file_name + " HTTP/1.1\r\n\r\n"
try:
	#send request
	s.send(request.encode())
except socket.error:
	print("Send Failed")
	sys.exit()

#receive data
reply = s.recv(10000)
print(reply)

s.close()


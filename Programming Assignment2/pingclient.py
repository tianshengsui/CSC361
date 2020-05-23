#import socket module
from socket import *
import sys # In order to terminate the program
import time

s = socket(AF_INET, SOCK_DGRAM)


IP_address = sys.argv[1]
port_number = int(sys.argv[2])

for i in range(1, 101):
	start = time.time()
	message = 'ping' + '    ' + str(i) + '    ' + str(start)
	s.sendto(message, (IP_address, port_number))

	response, addr = s.recvfrom(1024)
	end = time.time()
	while(response.isdigit()):
		print(response + "    Dropped!")
		message = 'ping' + '    ' + response + '    ' + str(start)
		s.sendto(message, (IP_address, port_number))
		response, addr = s.recvfrom(1024)
		end = time.time()
	rrt = end - start
	print(response + "    " + str(rrt) + " seconds")

s.close()

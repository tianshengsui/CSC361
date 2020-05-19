#import socket module
from socket import *
import sys # In order to terminate the program

try:
    #create an AF_INET, STREAM socket4
    serverSocket = socket(AF_INET, SOCK_STREAM)
except socket.error, msg:
    print("Failed to create socket. Error code: "+str(msg[0]) + ", Error message : "+msg[1])
    sys.exit()
print("Socket Created")

#Prepare a server socket
serverSocket.bind(("",6789))
serverSocket.listen(5)
print("Socket now listening")

while True:
    #Establish the connection
    print('Ready to serve...')
    #wait to accept a connection
    connectionSocket, addr =  serverSocket.accept()
    print("Connected with " + addr[0] + ":" + str(addr[1]))

    try:
        message = connectionSocket.recv(10000)
        filename = message.split()[1]                 
        f = open(filename[1:]) 

        outputdata = f.read()
        #Send one HTTP header line into socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        #Send the content of the requested file to the client
        for i in range(0, len(outputdata)):           
            connectionSocket.send(outputdata[i].encode())
        connectionSocket.send("\r\n".encode())
        
        connectionSocket.close()
    except IOError:
        #Send response message for file not found
        connectionSocket.send("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        #Close client socket
        connectionSocket.close()
        serverSocket.close()
        sys.exit()

serverSocket.close()
sys.exit()#Terminate the program after sending the corresponding data

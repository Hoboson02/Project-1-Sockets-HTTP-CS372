# import socket module
from socket import *

# In order to terminate the program. Not necessary.
import sys

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)
# Fill in start
serverPort = 10000
serverSocket = socket(AF_INET, SOCK_STREAM)
serverSocket.bind(('', serverPort))
serverSocket.listen(1)
# Fill in end

while True:
    print('The server is ready to receive')

    # Set up a new connection from the client
    # This is the client socket that gives information about the address
    connectionSocket, addr = serverSocket.accept()
    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request
        message = connectionSocket.recv(1024)
        print("Received:", message)
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]

        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:])
        # print('file opened')

        # Store the entire content of the requested file in a temporary buffer
        outputdata = f.read()

        # Send the HTTP response header line to the connection socket
        connectionSocket.send("HTTP/1.1 200 OK\r\n\r\n".encode())

        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())

        connectionSocket.send("\r\n".encode())

        # Close the client connection socket
        connectionSocket.close()

    except IOError:
        print('  *** file not found ***')
        # Send HTTP response message for file not found
        connectionSocket.send(
            "HTTP/1.1 404 Not Found\r\n\r\n".encode()
        )
        connectionSocket.close(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode()
        )

        # Close the client connection socket
        serverSocket.close()
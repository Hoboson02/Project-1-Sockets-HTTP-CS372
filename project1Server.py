# Import socket module from socket import *

# In order to terminate the program. Not necessary.
# import sys

# Create a TCP server socket
# (AF_INET is used for IPv4 protocols)
# (SOCK_STREAM is used for TCP)

serverSocket = socket(AF_INET, SOCK_STREAM)

#Fill in start
# Put some code in here
# Fill in end

while True:
    print('The server is ready to receive')
    
    # Set up a new connection from the client
    connectionSocket, addr = #Fill in start.    #Fill in end
    # If an exception occurs during the execution of try clause
    # the rest of the clause is skipped
    # If the exception type matches the word after except
    # the except clause is executed
    try:
        # Receives the request 
        message from the clientmessage = #Fill in start.    #Fill in end
        
        # Extract the path of the requested object from the message
        # The path is the second part of HTTP header, identified by [1]
        filename = message.split()[1]
        
        # Because the extracted path of the HTTP request includes
        # a character '\', we read the path from the second character
        f = open(filename[1:])
        # print('file opened')
        
        # Store the entire content of the requested file in a temporary buffer
        outputdata = #Fill in start.    #Fill in end
        
        # Send the HTTP response header line to the connection socket#Fill in start.    #Fill in end("HTTP/1.1 200 OK\r\n\r\n".encode())
        
        # Send the content of the requested file to the connection socket
        for i in range(0, len(outputdata)):
            connectionSocket.send(outputdata[i].encode())
            
        connectionSocket.send("\r\n".encode())
        
        # Close the client connection socket
        connectionSocket.close()
        
    except IOError:
        print('  *** file not found ***')
        # Send HTTP response message for file not found
        # #Fill in start.    #Fill in end
            ("HTTP/1.1 404 Not Found\r\n\r\n".encode())
        #Fill in start.    #Fill in end(
            "<html><head></head><body><h1>404 Not Found</h1></body></html>\r\n".encode())
        
        # Close the client connection socket
        #Fill in start.    #Fill in end
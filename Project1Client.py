# https://docs.python.org/3/library/socket.html
from socket import *
serverName = 'localhost'
serverPort = 10000
clientSocket = socket(AF_INET, SOCK_STREAM)
clientSocket.connect((serverName, serverPort))
library = "GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n"
clientSocket.send(library.encode())
host = "gaia.cs.umass.edu"
port = 80
while True:

    response = clientSocket.recv(1024)
    print('From Server:\n', response.decode())
clientSocket.close()
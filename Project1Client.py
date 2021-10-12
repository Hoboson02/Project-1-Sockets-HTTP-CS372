# https://docs.python.org/3/library/socket.html #Search for 'Echo server program' to find where formatting came from
from socket import *
# b' converts the string into a bytearray
file_location = b'GET /wireshark-labs/INTRO-wireshark-file1.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
# construction of the TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
host = "gaia.cs.umass.edu"
port = 80
clientSocket.connect((host, port))
clientSocket.send(file_location)
while True:
    response = clientSocket.recv(1024)
    if not response:
        break
    print(response.decode())
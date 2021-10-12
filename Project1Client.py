# https://docs.python.org/3/library/socket.html #Search for 'Echo server program' to find where formatting came from
from socket import *
# b' converts the string into a bytearray
file_location = b'GET /wireshark-labs/HTTP-wireshark-file3.html HTTP/1.1\r\nHost:gaia.cs.umass.edu\r\n\r\n'
# construction of the TCP socket
clientSocket = socket(AF_INET, SOCK_STREAM)
# establishing the host
host = "gaia.cs.umass.edu"
# establishing the port
port = 80
# Connecting the socket to the source
clientSocket.connect((host, port))
# send the data stored in file_location to the socket
clientSocket.send(file_location)
# As long as the client is able to fetch for bytes, continue to run
while True:
    response = clientSocket.recv(1024)
    if not response:
        break
        # print out the amalgamation of bytes collected from the loop
    print(response.decode())
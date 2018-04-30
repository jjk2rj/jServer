import socket
import sys
import argparse
import hashlib

# Parser for arguments
parser = argparse.ArgumentParser()

# Parse TCP port
# Default port: 2345 if not port is given
parser.add_argument('port', default= 2345, type=int, nargs='?')

# User arguments
args = parser.parse_args()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Bind the socket to the port
# Default IP address is 127.0.0.1
ip_address = '127.0.0.1'

server_address = (ip_address, args.port)
print('starting up on {}:{}'.format(*server_address))
sock.bind(server_address)

# Listen for incoming connections; one connection at a time
sock.listen(1)

while True:
    # Wait for a connection
    print('waiting for a connection')
    connection, client_address = sock.accept()

    # Receive hashing algorithm from client
    algo = (connection.recv(1))
    if algo == '0':
        algo = 'sha1'
    if algo == '1':
        algo = 'sha256'
    if algo == '2':
        algo = 'sha512'
    if algo == '3':
        algo = 'md5'
    print("Hashing algorithm: " + algo)
    hasher = hashlib.new(algo)

    received = 'received_from_client.txt'
    
    try:
        print('connection from', client_address)    
        while True:
            
            # Receive the data in 4096 byte chunks and retransmit it
            with open(received, 'wb') as fw:
                
                data = connection.recv(4096)
                
                # begin ---------
                if data:
                    print('received {!r}'.format(data))
                    fw.write(data)
                else:
                    break
            fw.close()
            print("Received!")
                    
            with open('received_from_client.txt', 'rb') as afile:
                buf = afile.read()
                hasher.update(buf)
            connection.send(hasher.hexdigest())
            
            # file_to_write.close()

            
    finally:
        # Clean up the connection
        connection.close()        
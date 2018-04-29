import socket
import sys
import argparse

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
    try:
        print('connection from', client_address)

        # Receive the data in 4096 byte chunks and retransmit it
        while True:
            data = connection.recv(4096)
            print('received {!r}'.format(data))
            # if data:
            #     print('sending data back to the client')
            #     connection.sendall(data)
            # else:
            #     print('no data from', client_address)
            #     break

    finally:
        # Clean up the connection
        connection.close()
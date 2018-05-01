import socket
import sys
import argparse
import hashlib
import threading

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
file_contents = ''
server_address = (ip_address, args.port)
print('starting up on {}:{}'.format(*server_address))
sock.bind(server_address)
#  ----- sock.connect(server_address)

# Listen for incoming connections; one connection at a time
sock.listen(1)
print('Listening on {}:{}'.format(ip_address, args.port))

def get_hash_algo(socket):
    hash_algo = socket.recv(1).decode()
    if hash_algo == '0':
        hash_algo = 'sha1'
    if hash_algo == '1':
        hash_algo = 'sha256'
    if hash_algo == '2':
        hash_algo = 'sha512'
    if hash_algo == '3':
        hash_algo = 'md5'
    print('Received {}'.format(hash_algo))
    return hash_algo

def receive_file(socket):
    file_chunk = socket.recv(4096).decode()
    print('Received {}'.format(file_chunk))
    return file_chunk
    # socket.send('ACK!')
    # client_socket.close()

def hash_file(file_contents):
    hasher = hashlib.new(hash_algo)
    hasher.update(file_contents.encode())
    hashed_file = hasher.hexdigest()
    return hashed_file




# Receive hashing algorithm from client
while True: 
    client_sock, client_address = sock.accept()
    print('Accepted connection from {}:{}'.format(client_address[0], client_address[1]))
    file_contents = ''
    hash_algo = get_hash_algo(client_sock)

    # with open(upload, 'wb') 
        # file_chunk = receive_file(client_sock)
        
    complete_file = ''
    while True: 
        file_chunk = client_sock.recv(4096).decode()
        if file_chunk == 'end':
            print('end')
        # file_chunk = receive_file(client_sock)
        # print(file_chunk)
        complete_file += file_chunk
        # print(file_chunk)

        if not file_chunk:
            print(complete_file)
            hashed = hash_file(complete_file)
            # client_sock.sendall(hashed.encode())
            print(hashed.encode())
            # client_sock.send(hashed.encode())
            break
    
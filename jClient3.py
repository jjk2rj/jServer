# j_client.py
import socket
import argparse
import hashlib
import sys
import os
# from ipaddress import ip_address

parser = argparse.ArgumentParser()

parser.add_argument(
    '-p',
    help='the name of the hash algorithm to use',
    default='2345',
    dest='port'
)

# Parse IP address
parser.add_argument('ip_address', 
    type=str,
    help = 'Enter an ip address, input a port number by placing a \':\' after the ip_address '
    )

# Parse hashing algorithm 
parser.add_argument(
    'hash_name',
    choices= ('sha1', 'sha256', 'sha512', 'md5'),
    help='the name of the hash algorithm to use',
    )

# Parse files names
# At least one file name is required
parser.add_argument(
    'file_names',
    nargs='+',
    help='the input data to hash',
    )

args = parser.parse_args()

# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (args.ip_address, int(args.port))
print('Connecting to {}:{}'.format(*server_address))
sock.connect(server_address)

# Obtain current working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))

# Send the data in each file
# Hash the contents of each file
for file in args.file_names:

    # Hashing algorithm obtained from user 
    hashed = hashlib.new(args.hash_name)
    f = open(os.path.join(__location__, file), 'r')
    # contents = f.read().encode('utf-8')
    message = f.read().encode('utf-8')

    # print hash of contents of file name of each file 
    hashed.update(message)
    # hashed_data = hashed.hexdigest()
    print(hashed.hexdigest() + " " + file)

    # Send data
    sock.sendall(message)

    amount_received = 0
    amount_expected = len(message)

    while amount_received < amount_expected:
        data = sock.recv(4096)  
        amount_received += len(data)
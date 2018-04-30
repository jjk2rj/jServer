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

algo = '7'
args = parser.parse_args()
if args.hash_name == 'sha1':
    algo = '0'
if args.hash_name == 'sha256':
    algo = '1'
if args.hash_name == 'sha512':
    algo = '2'
if args.hash_name == 'md5':
    algo = '3'


# Create a TCP/IP socket
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect the socket to the port where the server is listening
server_address = (args.ip_address, int(args.port))
print('Connecting to {}:{}'.format(*server_address))
sock.connect(server_address)

# Obtain current working directory
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))


# Send hashing algorithm to server
# print(args.hash_name)
# Hashing algorithm obtained from user 
hashed = hashlib.new(args.hash_name)
sock.send(algo)

# Send the data in each file
# Hash the contents of each file
for file in args.file_names:
    
    
    # open file and send data
    with open(os.path.join(__location__, file), 'rb') as f:

        data = f.read(4096)
    
        # print('Sending data', data)
        sock.send(data)

    # print("waiting for hash of file")
    data = sock.recv(4096)
    print(data + " " + file)

sock.close()
import socket
import argparse
import hashlib
import sys
import os
import io

file = '10kb.txt'
__location__ = os.path.realpath(
    os.path.join(os.getcwd(), os.path.dirname(__file__)))
# open file and send data
with open(os.path.join(__location__, file), 'rb') as f:
    
    data = f.read()
    
    # data_to_send = b'Foo' * 2000 # we must send bytes
    print('Data to send:', len(data))
    
    data = io.BytesIO(data)
    while True:
        chunk = data.read(4096)
        if not chunk:
            break
        # sock.send(chunk)
        print(chunk)
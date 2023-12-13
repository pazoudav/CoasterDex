import socket
import numpy as np
from pickle import dumps, loads
import time

HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
PORT = 65432  # Port to listen on (non-privileged ports are > 1023)
SIZE = 2**20

def receive_data(s: socket.socket):
    # print('waiting for request -', int(time.time()))
    info = s.recv(6)
    info = info.decode()
    if len(info) < 1:
        exit(0)
    info = int(info)
    data = b''
    while len(data) < info:
        new_data = s.recv(SIZE)
        data += new_data                
    assert len(data) == info
    data = loads(data)
    return data

def send_data(s : socket.socket, data):
    data = dumps(data)
    info = f'{len(data)}'.encode()
    # print('sending:', len(info), len(data))
    s.send(info)
    s.sendall(data)

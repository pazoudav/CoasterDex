import socket
from pickle import loads, dumps
import numpy as np
from matcher.serverHelper import *
from matcher.coasterMatcher import CoasterMatcher


matcher = CoasterMatcher()
print('matcher loaded')

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
    s.bind((HOST, PORT))
    s.listen()
    conn, addr = s.accept()
    with conn:
        print(f"Connected by {addr}")
        while True:
            # print('receiving')
            data = receive_data(conn)
            # print('matching')
            data = matcher.match(data, k=3)
            # print('sending')
            send_data(conn, data)
            # print('done')
            

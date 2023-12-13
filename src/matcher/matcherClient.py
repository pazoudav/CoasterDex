import socket
import select
import numpy as np
import cv2 as cv
from matcher.serverHelper import *
import time

class MatcherClient:
    def __init__(self) -> None:
        self.socket = socket.socket() 
        self.socket.connect((HOST, PORT)) 
        self.send = False

        
    def close(self):
        self.socket.close()
        
    def match(self, img, **kwargs):
        matcher_data = None
        if not self.send:
            self.send = True
            # print('sending')
            send_data(self.socket, np.array(img))
        if self.send:
            read_sockets, _, _ = select.select([self.socket] , [], [], 0.001)
            # if len(read_sockets) == 0:
                # print('skipped receive')
            for s in read_sockets:
                # print('receiving')
                matcher_data = receive_data(s)
                self.send = False
                # print('matched')
        return matcher_data


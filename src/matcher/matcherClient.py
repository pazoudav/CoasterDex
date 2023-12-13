import socket
import numpy as np
import cv2 as cv
from matcher.serverHelper import *
import time

class MatcherClient:
    def __init__(self) -> None:
        self.socket = socket.socket() 
        self.socket.connect((HOST, PORT)) 
        
    def close(self):
        self.socket.close()
        
    def match(self, img, **kwargs):
        print('sending')
        send_data(self.socket, np.array(img))
        print('receiving')
        matcher_data = receive_data(self.socket)
        print('matched')
        return matcher_data

# img = cv.imread('C:\\Users\\pazou\\Documents\\CVUT\\COMP\\project\\dataset\\coaster-photos\\1.jpg')
# data = np.array(img)

# with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
#     print('connecting')
#     s.connect((HOST, PORT))
#     print('sending')
#     send_data(s, data)
#     data2 = receive_data(s)
#     # time.sleep(10)
# print(f"Received:\n{data2}")
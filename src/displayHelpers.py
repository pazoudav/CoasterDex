import time
import cv2 as cv
import numpy as np
from matcher.helper import resize_to_width, folder_iterator, open_image

font = cv.FONT_HERSHEY_SIMPLEX 
now = time.time() 
 
# helper class for image input
class ImageInput:
	def __init__(self, path):
		self.img = cv.imread(path)
	def read(self):
		return True, self.img.copy()

class FolderInput:
	def __init__(self, path):
		self.path = path
		self.files = [f for f in folder_iterator(path)]
		self.idx = 0

	def read(self):
		# self.idx = self.idx%len(self.files)
		file = self.files[self.idx]
		self.idx += 1

		img, name = open_image(file)
		return self.idx < len(self.files), img
 
 
def tick():
	global now
	delta = time.time() - now
	now = time.time()
	if delta <  0.001:
		delta = 0.001
	return delta

def add_fps(img):
	fps = 1/tick() # int(1/tick()) # 
	cv.putText(img, f'{fps:.2f}', (10,30), font, 1, (0,0,255), 2, cv.LINE_AA)
	return fps

def display_matches(matcher_data : dict, args, k=3, name='0'):
	n = min(k, len(matcher_data['matches']))
	for idx, image in enumerate(matcher_data['matches'][:n]):
		matcher_data['matches'][idx] = resize_to_width(image, 200)
	if n > 0:
		img = np.vstack(matcher_data['matches'][:n])
		if 'm_mkp' in args.display:
			display_points(img, matcher_data['scan key points'], size=4, color=(0,255,0))
		cv.putText(img, f"# of kp: {len(matcher_data['scan key points'])}/{len(matcher_data['matched key points'])}/{len(matcher_data['key points'])}", (5,30), font, 0.5, (0,255,0), 1, cv.LINE_AA)
		cv.imshow(f'matches_{name}', img)
	
def display_points(img, points, color=(255,0,0), size=10):
	for point in points:
		cv.drawMarker(img, point.astype(int), color, markerType=cv.MARKER_CROSS, markerSize=size, thickness=1)
	   
	   

def find_bounding_box(points, percentile=0.8):
	if len(points) > 2:
		x_coordinates, y_coordinates = zip(*points.astype(int))
		x_coordinates = sorted(x_coordinates)
		y_coordinates = sorted(y_coordinates)
		# take 80th percentile of the data
		eps = (1-percentile)/2
		start = int(len(x_coordinates)*eps)
		end   = int(len(x_coordinates)*(1-eps))
		x0, y0, x1, y1 = x_coordinates[start], y_coordinates[start], x_coordinates[end], y_coordinates[end]
		# enlarge the bounding box by a factor of 1.5
		sx = (x0+x1)//2
		sy = (y0+y1)//2
		dx = int(1.5*(x1-x0)/2)
		dy = int(1.5*(y1-y0)/2)
		return (sx-dx, sy-dy), (sx+dx, sy+dy)
	return (-10,-10), (10000,10000)
		
def add_bounding_box(img, points):
	start_point, end_point = find_bounding_box(points)
	cv.rectangle(img, start_point, end_point, (0,255,0), 1)
	
  
def select_rectangle_wrapper(img, callback_func):
	ix, iy = -1, -1 
	def select_rectangle(event, x, y, flags, param):
		global ix, iy
		if event == cv.EVENT_LBUTTONDOWN:
			ix = x
			iy = y
		elif event == cv.EVENT_LBUTTONUP:
			bbox = ((ix, iy),(x, y))
			callback_func(img, bbox, 'aaaa')
			cv.destroyWindow('freeze_frame')
			ix, iy = -1, -1 
		elif event == cv.EVENT_MOUSEMOVE:
			try:
				if ix != -1:
					r_img = cv.rectangle(img.copy(), (ix,iy), (x,y), (0,255,0), 2)
					cv.imshow('freeze_frame', r_img)
			except NameError:
				...
				
	return select_rectangle


def freeze_display(img, callback_func):
	cv.namedWindow("freeze_frame")
	cv.setMouseCallback("freeze_frame", select_rectangle_wrapper(img, callback_func))
	cv.imshow('freeze_frame', img)


def display_matcher_data(img, matcher_datas, args, offset=(0,0), name='0'):
	if args.no_display:
		return
	for idx, matcher_data in enumerate(matcher_datas):
		if len(matcher_data['scan key points']) >= 16:
			display_matches(matcher_data, args, name=idx)
			if 'm_bbox' in args.display:
				add_bounding_box(img, matcher_data['matched key points'])
		if 'm_kp' in args.display:
			display_points(img, matcher_data['key points'])
		if 'm_mkp' in args.display:
			display_points(img, matcher_data['matched key points'], color=(0,255,0)) 
   
	
def display_bboxs(img, bboxs, args):
	if 'f_bbox' in args.display:
		for bbox in bboxs:
			s,e = bbox
			cv.rectangle(img, s, e, (0,0,255), 2)
				
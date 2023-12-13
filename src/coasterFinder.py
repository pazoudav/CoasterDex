import cv2 as cv
import numpy as np

# Constants.
INPUT_WIDTH = 640
INPUT_HEIGHT = 640
SCORE_THRESHOLD = 0.5
NMS_THRESHOLD = 0.45
CONFIDENCE_THRESHOLD = 0.45

# Text parameters.
FONT_FACE = cv.FONT_HERSHEY_SIMPLEX
FONT_SCALE = 0.7
THICKNESS = 1

# Colors
BLACK  = (0,0,0)
BLUE   = (255,178,50)
YELLOW = (0,255,255)
RED = (0,0,255)

classes = ['Coaster'] # detection classes

class CoasterFinder:
    """ Returns bounding boxes of coasters in image in an array where bounding box has 2 points, tuples, p1 and p4, right upper corner and lower left corner respectively """

    def __init__(self,path=None):
        modelWeights = "coasterDetect.onnx"
        self.net = cv.dnn.readNet(modelWeights)

    def find(self, img, **kwargs):
        bbox = self.coaster_boxes(img)
        return bbox, 

    def coaster_boxes(self, img):

        #img = compress(img)
        # load model
        detections = pre_process(img, self.net)
        image, bboxes = post_process(img.copy(), detections)

        """ Inference time check
        t, _ = net.getPerfProfile() 
        label = 'Inference time: %.2f ms' % (t * 1000.0 / cv.getTickFrequency())
        print(label) """
        if bboxes != []:
            print(bboxes)

        return bboxes

def draw_label(input_image, label, left, top):
    """Draw text onto image at location."""
    
    # Get text size.
    text_size = cv.getTextSize(label, FONT_FACE, FONT_SCALE, THICKNESS)
    dim, baseline = text_size[0], text_size[1]
    # Use text size to create a BLACK rectangle. 
    cv.rectangle(input_image, (left, top), (left + dim[0], top + dim[1] + baseline), BLACK, cv.FILLED)
    # Display text inside the rectangle.
    cv.putText(input_image, label, (left, top + dim[1]), FONT_FACE, FONT_SCALE, YELLOW, THICKNESS, cv.LINE_AA)


def pre_process(input_image, net):
    # Create a 4D blob from a frame.
    blob = cv.dnn.blobFromImage(input_image, 1/255, (INPUT_WIDTH, INPUT_HEIGHT), [0,0,0], 1, crop=False)

    # Sets the input to the network.
    net.setInput(blob)

    # Runs the forward pass to get output of the output layers.
    output_layers = net.getUnconnectedOutLayersNames()
    outputs = net.forward(output_layers)
    # print(outputs[0].shape)

    return outputs


def post_process(input_image, outputs):
    # Lists to hold respective values while unwrapping.
    class_ids = []
    confidences = []
    boxes = []

    # Rows.
    rows = outputs[0].shape[1]

    image_height, image_width = input_image.shape[:2]

    # Resizing factor.
    x_factor = image_width / INPUT_WIDTH
    y_factor =  image_height / INPUT_HEIGHT

    # Iterate through 25200 detections.
    for r in range(rows):
        row = outputs[0][0][r]
        confidence = row[4]

        # Discard bad detections and continue.
        if confidence >= CONFIDENCE_THRESHOLD:
            classes_scores = row[5:]

            # Get the index of max class score.
            class_id = np.argmax(classes_scores)

            #  Continue if the class score is above threshold.
            if (classes_scores[class_id] > SCORE_THRESHOLD):
                confidences.append(confidence)
                class_ids.append(class_id)

                cx, cy, w, h = row[0], row[1], row[2], row[3]

                left = int((cx - w/2) * x_factor)
                top = int((cy - h/2) * y_factor)
                width = int(w * x_factor)
                height = int(h * y_factor)
            
                box = np.array([left, top, width, height])
                boxes.append(box)

    # Perform non maximum suppression to eliminate redundant overlapping boxes with
    # lower confidences.
    bboxes = [] # bounding boxes
    indices = cv.dnn.NMSBoxes(boxes, confidences, CONFIDENCE_THRESHOLD, NMS_THRESHOLD)
    for i in indices:
        box = boxes[i]
        left = box[0]
        top = box[1]
        width = box[2]
        height = box[3]
        p1, p2, p3, p4 = (left,top),(left + width, top), (left, top + height), (left + width, top + height)
        bboxes.append([p1,p4])
        cv.rectangle(input_image, (left, top), (left + width, top + height), BLUE, 3*THICKNESS)
        label = "{}:{:.2f}".format(classes[class_ids[i]], confidences[i])
        draw_label(input_image, label, left, top)

    return input_image, bboxes

def compress(img):

    width = 640
    height = 360
    resized = cv.resize(img,(width,height))

    return img




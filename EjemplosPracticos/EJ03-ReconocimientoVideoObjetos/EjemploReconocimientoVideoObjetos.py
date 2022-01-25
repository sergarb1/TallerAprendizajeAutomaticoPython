#!/usr/bin/python3

#pip3 install opencv-python pillow tensorflow cvlib

import cv2
import cvlib as cv
from cvlib.object_detection import draw_bbox

# Enable camera
cap = cv2.VideoCapture(0)
cap.set(3, 640)
cap.set(4, 420)

while True:
    success, img = cap.read()

    bbox, label, conf = cv.detect_common_objects(img)
    print('Number of keyboards in the image is '+ str(label.count('keyboard')))

    output_image = draw_bbox(img, bbox, label, conf)
    
    cv2.imshow('cars_detect', output_image)
    if cv2.waitKey(10) & 0xFF == ord('q'):
        break
cap.release()
cv2.destroyWindow('cars_detect')


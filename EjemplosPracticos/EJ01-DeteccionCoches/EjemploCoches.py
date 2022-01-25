#!/usr/bin/python3


#pip3 install --upgrade opencv-python pillow tensorflow cvlib numpy
#OJO Error con version moderna de opencv-python https://stackoverflow.com/questions/69719025/cvlib-causing-indexerror-invalid-index-to-scalar-variable
#Se arregla con pip3 install opencv-python==4.5.3.56)

import cv2
import matplotlib.pyplot as plt
import cvlib as cv
from cvlib.object_detection import draw_bbox


im = cv2.imread('cars_4.jpg')

bbox, label, conf = cv.detect_common_objects(im)
output_image = draw_bbox(im, bbox, label, conf)
plt.imshow(output_image)
plt.show()
print('Number of cars in the image is '+ str(label.count('car')))

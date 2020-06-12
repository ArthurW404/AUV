"""
Sample probablistic hough line tranform using opencv

"""

import cv2
import numpy as np

# read image
img = cv2.imread('../images/gate.jpg')

# convert image to grayscale
gray = cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)

#get edges 
edges = cv2.Canny(gray,50,150,apertureSize = 3)
minLineLength = 100
maxLineGap = 10

# get lines using probabilistic hough transform
lines = cv2.HoughLinesP(edges,1,np.pi/180,100,minLineLength,maxLineGap)

# add lines to image
for line in lines:
    x1,y1,x2,y2 = line[0]
    print(x1,y1,x2,y2)
    cv2.line(img,(x1,y1),(x2,y2),(0,0,255),2)

cv2.imwrite('houghlines5.jpg',img)


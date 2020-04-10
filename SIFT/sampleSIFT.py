import cv2
import numpy as np

image = cv2.imread('leaf.jpg')
image = cv2.resize(image, (1200,900))
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# create SIFT Feature Detector object
sift = cv2.xfeatures2d.SIFT_create()

#Detect Key points
keypoints = sift.detect(gray, None)
print("Number of keypoints detected: ", len(keypoints))

#Draw rich key points on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, outImage=None)

cv2.imshow('Feature Method- SIFT', image)
cv2.waitKey(0) 
cv2.destroyAllWindows()
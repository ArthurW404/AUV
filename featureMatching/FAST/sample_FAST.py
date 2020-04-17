import cv2
import numpy as numpy

image = cv2.imread('gate.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

#create fast detector object
fast = cv2.FastFeatureDetector_create()

# Obtain key points using FAST
keypoints = fast.detect(gray, None)
num_kpts = len(keypoints)
print(f"Number of keypoints Detected: {num_kpts}")
print(keypoints[0])
# extract key points as list 
pts = cv2.KeyPoint_convert(keypoints)
print(pts[0])

# draw rich keypoints on input image
image = cv2.drawKeypoints(gray, keypoints, outImage=None, color=[0, 0, 255],flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

image = cv2.resize(image, (1400, 900))
cv2.imwrite('FAST.jpg', image)
cv2.waitKey()
cv2.destroyAllWindows()
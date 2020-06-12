import cv2  
import numpy as np

image = cv2.imread('leaf.jpg')

gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# Create SURF Feature Detector object
# Only features, whose hessian is larger than hessianThreshold are retained by the detector
surf = cv2.xfeatures2d.SURF_create(2000)

keypoints, descriptors = surf.detectAndCompute(gray, None)
print("Number of keypoints Detected: ", len(keypoints))

# Draw rich key points on input image
image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, outImage=None)
image = cv2.resize(image, (1200,900))
cv2.imshow('Feature Method - SURF', image)
cv2.waitKey()
cv2.destroyAllWindows()
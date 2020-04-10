import cv2
import numpy as np

image = cv2.imread('gate.jpg')
gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# create FAST detector object
fast = cv2.xfeatures2d.StarDetector_create()

# create BRIF extractor object
brief = cv2.xfeatures2d.BriefDescriptorExtractor_create()

# Determine key points
keypoints = fast.detect(gray, None)

keypoints, descriptors = brief.compute(gray, keypoints)
print(f"Number of keypoints Detected: {len(keypoints)}")

image = cv2.drawKeypoints(image, keypoints, flags=cv2.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS, outImage=None, color=[0,0,255])

image = cv2.resize(image, (1400, 900))
cv2.imshow('BRIEF', image)
cv2.waitKey()
cv2.destroyAllWindows()
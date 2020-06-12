import cv2
import numpy as np
from matplotlib import pyplot as plt

image = cv2.imread('../images/buckets.jpg', 0)

# Initiate STAR detector
orb = cv2.ORB_create()

# Determine key points
keypoints = orb.detect(image, None)

keypoints, descriptors = orb.compute(image, keypoints)
print(f"Number of keypoints Detected: {keypoints}")

image = cv2.drawKeypoints(image, keypoints, flags=0, outImage=None, color=[0,0,255])

plt.imshow(image)
plt.savefig("mygraph.png")
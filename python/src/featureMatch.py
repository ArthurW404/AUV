import numpy as np
import cv2 as cv

def FAST(image):
    gray = cv.cvtColor(image, cv.COLOR_BGR2GRAY)

    #create fast detector object
    fast = cv.FastFeatureDetector_create()

    # Obtain key points using FAST
    keypoints = fast.detect(gray, None)
    # num_kpts = len(keypoints)
    # print(f"Number of keypoints Detected: {num_kpts}")
    # print(keypoints[0])
    # extract key points as list 
    # pts = cv.KeyPoint_convert(keypoints)
    # print(pts[0])

    # draw rich keypoints on input image
    image = cv.drawKeypoints(image, keypoints, outImage=None, color=[0, 0, 255],flags=cv.DRAW_MATCHES_FLAGS_DRAW_RICH_KEYPOINTS)

    image = cv.resize(image, (1400, 900))
    return image
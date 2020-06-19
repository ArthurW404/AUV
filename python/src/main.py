#!/usr/bin/python3
"""
    Main function of computer vision system
"""
import numpy as np
import cv2 as cv
from featureMatch import FAST

if __name__ == "__main__":
    cap = cv.VideoCapture(0)

    while(True):
        # Capture frame-by-frame
        ret, frame = cap.read()

        corners = FAST(frame)
        # Our operations on the frame come here
        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Display the resulting framef
        cv.imshow('frame',corners)
        if cv.waitKey(1) & 0xFF == ord('q'):
            break

    # When everything done, release the capture
    cap.release()
    cv.destroyAllWindows()
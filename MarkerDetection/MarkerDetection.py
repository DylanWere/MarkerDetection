3
import cv2 as cv
import numpy as np
import cv2.aruco as aruco
from utils import ARUCO_DICT, DEFAULTS_DICT, aruco_display
from Calibrate import Calibrate
from GenerateTags import GenerateTags



class MarkerDetector:
    def __init__(self):
        self.marker = aruco.getPredefinedDictionary(DEFAULTS_DICT["DEFAULT_ARUCO_DICT"])

    def detect(self):
        #get a dictionary of what m,arkers are needed
        arucoDict = self.marker
        #set parameters (default)
        arucoParams = aruco.DetectorParameters_create()
        #start capturing video
        vid_capture = cv.VideoCapture(0)


        while (vid_capture.grab()):
            #ret is whether the connection is good, frame is the fram from the camera
            ret, inputImage = vid_capture.read()
            #exit if connection is bad
            if ret == False: 
                break
            (markerCorners, markerIDs, rejected) = cv.aruco.detectMarkers(inputImage, arucoDict, parameters=arucoParams)
            
            detected_markers = aruco_display(markerCorners, markerIDs, rejected, inputImage)
            
            aruco.drawDetectedMarkers(inputImage, markerCorners, markerIDs)

            cv.imshow("out", inputImage)
            #wait for 'q' key to exit
            if cv.waitKey(1) & 0xFF == ord('q'):
                break
        vid_capture.release()
        cv.destroyAllWindows()








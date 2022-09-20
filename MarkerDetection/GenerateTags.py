import cv2 as cv
import cv2.aruco as aruco
import numpy as np
import argparse
from utils import ARUCO_DICT, DEFAULTS_DICT
import sys
import tkinter as tk
from   tkinter import filedialog

class GenerateTags:
    def __init__(self):

        print('Please choose the directory where the ArUCo tag will be saved')
        print('Press enter to continue')
        input()
        root = tk.Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory()
        print(dirpath)

        good = False
        while good == False:
            print('Please enter the ID of ArUCo tag to generate: ')
            iden = int(input())
            if iden <= 0:
                print('Error: Please enter a positive number')
                continue
            good = True

        good = False
        while good == False:
            print('Please enter the type of ArUCo tag to generate: ')
            tagType = input()
            if ARUCO_DICT.get(tagType) is None:
                print(f"AruCo tag type 'tagType' is not supported")
                continue
            good = True
        
        good = False
        while good == False:
            print('Please enter the size of ArUCo tag to generate: ')
            size = int(input())
            if size <= 0:
                print('Error: Please enter a positive number')
                continue
            good = True

        # Check to see if the dictionary is supported
        

        arucoDict = aruco.Dictionary_get(ARUCO_DICT[tagType])

        print("Generating ArUCo tag of type '{}' with ID '{}'".format(tagType, iden))
        tag_size = size
        tag = np.zeros((tag_size, tag_size, 1), dtype="uint8")
        cv.aruco.drawMarker(arucoDict, iden, tag_size, tag, 1)

        # Save the tag generated
        tag_name = f'{dirpath}/{tagType}_id_{iden}.png'
        cv.imwrite(tag_name, tag)
        cv.imshow("ArUCo Tag", tag)
        cv.waitKey(0)
        cv.destroyAllWindows()


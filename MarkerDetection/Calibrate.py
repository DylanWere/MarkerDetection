import numpy as np
import cv2 as cv
import os
import argparse
import tkinter as tk
from   tkinter import filedialog

class Calibrate:
    def __init__(self):

        print('Please choose the folder where the checkerboard images are located')
        print('Press enter to continue')
        input()
        root = tk.Tk()
        root.withdraw()
        dirpath = filedialog.askdirectory()
        print(dirpath)

        
        good = False
        while good == False:
            print('Please enter the width of the checkerboard: ')
            width = input()
            good = True
            if not width.isnumeric():
                print('Error: Please enter a number')
                continue
            if width <= 0:
                print('Error: Please enter a positive number')
                continue


        good = False
        while good == False:
            print('Please enter the height of the checkerboard: ')
            height = input()
            good = True
            if not width.isnumeric():
                print('Error: Please enter a number')
                continue
            if width <= 0:
                print('Error: Please enter a positive number')
                continue
       
        good = False
        while good == False:
            print('Please enter the size of the squares: ')
            square_size = input()
            good = True
            if not width.isnumeric():
                print('Error: Please enter a number')
                continue
            if width <= 0:
                print('Error: Please enter a positive number')
                continue
    
        # 2.4 cm == 0.024 m
        # square_size = 0.024

        good = False
        while good == False:
            print('visualise? True or False: ')
            visualize = input()
            good = True
            if not width.isnumeric():
                print('Error: Please enter a number')
                continue
            if width <= 0:
                print('Error: Please enter a positive number')
                continue

        if visualize.lower() == "true":
            visualize = True
        else:
            visualize = False

        ret, mtx, dist, rvecs, tvecs = self.__calibrate(dirpath, square_size, visualize=visualize, width=width, height=height)

        print(mtx)
        print(dist)

        np.save("calibration_matrix", mtx)
        np.save("distortion_coefficients", dist)

    def __calibrate(dirpath, square_size, width, height, visualize=False):
        """ Apply camera calibration operation for images in the given directory path. """

        # termination criteria
        criteria = (cv.TERM_CRITERIA_EPS + cv.TERM_CRITERIA_MAX_ITER, 30, 0.001)

        # prepare object points, like (0,0,0), (1,0,0), (2,0,0) ....,(8,6,0)
        objp = np.zeros((height*width, 3), np.float32)
        objp[:, :2] = np.mgrid[0:width, 0:height].T.reshape(-1, 2)

        objp = objp * square_size

        # Arrays to store object points and image points from all the images.
        objpoints = []  # 3d point in real world space
        imgpoints = []  # 2d points in image plane.

        images = os.listdir(dirpath)

        for fname in images:
            img = cv.imread(os.path.join(dirpath, fname))
            gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)

            # Find the chess board corners
            ret, corners = cv.findChessboardCorners(gray, (width, height), None)

            # If found, add object points, image points (after refining them)
            if ret:
                objpoints.append(objp)

                corners2 = cv.cornerSubPix(gray, corners, (11, 11), (-1, -1), criteria)
                imgpoints.append(corners2)

                # Draw and display the corners
                img = cv.drawChessboardCorners(img, (width, height), corners2, ret)

            if visualize:
                cv.imshow('img',img)
                cv.waitKey(0)


        ret, mtx, dist, rvecs, tvecs = cv.calibrateCamera(objpoints, imgpoints, gray.shape[::-1], None, None)

        return [ret, mtx, dist, rvecs, tvecs]


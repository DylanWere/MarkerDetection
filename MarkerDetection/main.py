import numpy as np
import cv2 as cv
import os
import argparse
import tkinter as tk
from MarkerDetection import MarkerDetector
from Calibrate import Calibrate
from GenerateTags import GenerateTags
from tkinter import filedialog


def main():
    while True:
        print('please choose a number')
        print('1 : Calibrate Camera')
        print('2 : Detect Markers')
        print('3 : Generate Tags')
        selection = input()
        selection = int(selection)
        if selection == 1:
            print(selection)
            Calibrate()
        if selection == 2:
            arucoDetect = MarkerDetector()
            arucoDetect.detect()
        if selection == 3:
            GenerateTags()

    

if __name__ == "__main__":
    main()

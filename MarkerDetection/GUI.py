from ast import Lambda
from turtle import left
import numpy as np
import cv2 as cv
import os
import argparse
from   tkinter import *
import tkinter as tk
from tkinter import ttk
from tkinter import filedialog
from utils import ARUCO_DICT
from GenerateTags import GenerateTags

class Gui:

    welcomeMessage = "Hi! welcome to group fourexplore's pose detection system read below to get started."
    genTagsMessage = "Generate tags will create a file which you can use to print out a tag, using this tag in the next stages will enable you to estimate\nthe pose of the tag in 3D space!"
    calibrateMessage = "This tab allows for our program to get a better understand of where your tag is in space, calibrating the camera is a necessary\nphase before you can continue to Detect Pose."
    detectPoseMessage = "This tab will use the camera to tell you just where the tag is in 3D space."

    navbarOptions = {"home":"Home", "camera" : "Camera Settings", "generate" : "Generate Markers", "calibrate" : "Calibrate", "detect" : "Detect Pose"}

    txtBodyFormatting = 'TkDefaultFont 16'
    txtHeadingFormatting = 'TkDefaultFont 18 bold'


    def __init__(self):
        self.state = self.navbarOptions["home"]
        self.window = Tk()
        self.window.geometry("1200x800+0+0")
        self.camSettingsRun = False
        self.getCamList()
        self.mainDisplayFrame = tk.Frame()
        self.gui_navbar()
        self.draw_home()
        self.window.mainloop()
        
    
    def draw(self, tab):
        self.mainDisplayFrame.forget()
        self.mainDisplayFrame.destroy()
        


        if(tab == self.navbarOptions["home"]):
            self.state = self.navbarOptions["home"]
            self.draw_home()
        if(tab == self.navbarOptions["camera"]):
            self.state = self.navbarOptions["camera"]
            self.draw_camera()
        if(tab == self.navbarOptions["generate"]):
            self.state = self.navbarOptions["generate"]
            self.draw_generate()
        if (tab == self.navbarOptions["calibrate"]):
            self.state = self.navbarOptions["calibrate"]
            self.draw_calibrate()
        if (tab == self.navbarOptions["detect"]):
            self.state = self.navbarOptions["detect"]
            self.draw_detect()

    def gui_navbar(self):
        topFrame = Frame(
            master = self.window,
            bg = "white")
        topFrame.pack(
            side = "top",
            fill = tk.X)
        Button(topFrame, text=self.navbarOptions["home"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["home"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        Button(topFrame, text=self.navbarOptions["camera"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["camera"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        Button(topFrame, text=self.navbarOptions["generate"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["generate"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        Button(topFrame, text=self.navbarOptions["calibrate"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["calibrate"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        Button(topFrame, text=self.navbarOptions["detect"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["detect"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)

    def draw_home(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,)
        self.mainDisplayFrame.pack(side="top")
        Label(master=self.mainDisplayFrame, text=self.welcomeMessage, pady=50,font=self.txtBodyFormatting).pack(anchor=tk.W)
        Label(master=self.mainDisplayFrame, text=self.navbarOptions["generate"], font=self.txtHeadingFormatting).pack(anchor=tk.W)
        Label(master=self.mainDisplayFrame, text=self.genTagsMessage, pady=10, font=self.txtBodyFormatting, justify="left").pack(anchor=tk.W)
        Label(master=self.mainDisplayFrame, text=self.navbarOptions["calibrate"], font=self.txtHeadingFormatting).pack(anchor=tk.W)
        Label(master=self.mainDisplayFrame, text=self.calibrateMessage, pady=10, font=self.txtBodyFormatting, justify="left").pack(anchor=tk.W)
        Label(master=self.mainDisplayFrame, text=self.navbarOptions["detect"], font=self.txtHeadingFormatting).pack(anchor=tk.W)
        Label(master=self.mainDisplayFrame, text=self.detectPoseMessage, pady=10, font=self.txtBodyFormatting).pack(anchor=tk.W)

    def draw_camera(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,)
        self.mainDisplayFrame.pack()

        #choose camera
        Label(master=self.mainDisplayFrame, text='Please choose the camera you wish to use', pady=50,font=self.txtBodyFormatting).grid(column=0, row=0, ipadx=10)


        #create combobox of cameras
        chosenCam = StringVar()
        self.camCB = ttk.Combobox(self.mainDisplayFrame, textvariable=chosenCam, width=20)
        self.camCB['values'] = [m for m in self.cameraList]
        self.camCB['state'] = 'readonly'
        self.camCB.set("Pick an Option")
        self.camCB.bind("<<ComboboxSelected>>", self.setCam)
        self.camCB.grid(column=1, row=0, ipadx=10)

        Label(master=self.mainDisplayFrame, text='Preview Camera:', pady=50,font=self.txtBodyFormatting).grid(column=0, row=1, ipadx=10)
        #create button
        button = Button(master=self.mainDisplayFrame, text="...", activebackground="gray99", activeforeground="gray50", font=self.txtBodyFormatting, command=self.previewCamera )
        button.grid(column=1, row=1, ipadx=10)

        Label(master=self.mainDisplayFrame, text='Camera Resolution:', pady=50,font=self.txtBodyFormatting).grid(column=0, row=2, ipadx=10)
        
        #create combobox of camera resolutions
        resOptions = ["1: Standard 480p [ 640, 480]", "2: High 720p     [1280, 720]", "3: Full HD 1080p [1920,1080])"]
        camResolution = StringVar()
        self.resolutionCB = ttk.Combobox(self.mainDisplayFrame, textvariable=camResolution, width=20)
        self.resolutionCB['values'] = [resOptions]
        self.resolutionCB['state'] = 'readonly'
        self.resolutionCB.set("Resolution Types")
        self.resolutionCB.bind("<<ComboboxSelected>>", self.setCam)
        self.resolutionCB.grid(column=1, row=2, ipadx=10)

        self.camSettingsRun = True

    def previewCamera(self):
        if (self.camCB.get() == ""):
            return
        else:
            index = int(self.camCB.get())
            cap = cv.VideoCapture(index)
            while True:
                ret, frame = cap.read()
                cv.imshow("Camera index {} - Press q to close".format(index), frame) 
                key = cv.waitKey(1) & 0xFF 
                if key == ord("q"): break
            cap.release()
            cv.destroyAllWindows()

    def setCam(self):
        if (self.camCB.get() == ""):
            self.camSet = False
        else:
            self.camIndex = self.camCB.get()
            self.camSet = True

    def getCamList(self):
        #get a list of cameras
        self.cameraList = []
        for i in range(10):
            cap = cv.VideoCapture(i)
            if (cap.read()[0]):
                self.cameraList.append(i)
                cap.release()

    def draw_generate(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,)
        self.mainDisplayFrame.pack()


        Label(master=self.mainDisplayFrame, text='Please choose the directory where the ArUCo tag will be saved', pady=50,font=self.txtBodyFormatting).grid(column=0, row=0)
        Button(master=self.mainDisplayFrame, text="...", activebackground="gray99", activeforeground="gray50", font=self.txtBodyFormatting, command=self.get_dirpath ).grid(column=1, row=0)
        

        Label(master=self.mainDisplayFrame, text='Please enter the ARuCo Dictionary:', pady=50,font=self.txtBodyFormatting).grid(column=0, row=1)

        chosenDict = StringVar()
        self.dictCB = ttk.Combobox(self.mainDisplayFrame, textvariable=chosenDict, width=20)
        self.dictCB['values'] = [m for m in ARUCO_DICT]
        self.dictCB['state'] = 'readonly'
        self.dictCB.grid(column=1, row=1, ipadx=10)

        Label(master=self.mainDisplayFrame, text='Please enter the ID of the tag(1, 2, 3, 4, ... etc.):', pady=50,font=self.txtBodyFormatting, justify='left').grid(column=0, row=2)

        self.arucoTagIDText = Entry(master=self.mainDisplayFrame, width = 10)
        self.arucoTagIDText.grid(column=1, row=2)
        
        Label(master=self.mainDisplayFrame, text='Please enter the size of the tag:', pady=50,font=self.txtBodyFormatting).grid(column=0, row=3)

        self.arucoTagSizeText = Entry(master=self.mainDisplayFrame, width = 10)
        self.arucoTagSizeText.grid(column=1, row=3)

        Button(master=self.mainDisplayFrame, text="Generate Tag", activebackground="gray99", activeforeground="gray50", font=self.txtBodyFormatting, command=self.generate_params ).grid(column=2, row=4, padx=20)

    def generate_params(self):
        self.arucoDict = self.dictCB.get()
        self.arucoTagID = self.arucoTagIDText.get()
        self.arucoTagSize = self.arucoTagSizeText.get()
        #GenerateTags()

    def get_dirpath(self):
        root = tk.Tk()
        root.withdraw()
        self.tagDirpath = filedialog.askdirectory()


    def draw_calibrate(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="dark olive green")
        self.mainDisplayFrame.pack()

        Label(master=self.mainDisplayFrame, text='Please choose the directory where the ArUCo tag will be saved', pady=50,font=self.txtBodyFormatting).grid(column=0, row=0)
        Button(master=self.mainDisplayFrame, text="...", activebackground="gray99", activeforeground="gray50", font=self.txtBodyFormatting, command=self.get_dirpath ).grid(column=1, row=0)
        

        Label(master=self.mainDisplayFrame, text='Please enter the ARuCo Dictionary:', pady=50,font=self.txtBodyFormatting).grid(column=0, row=1)

        chosenDict = StringVar()
        self.dictCB = ttk.Combobox(self.mainDisplayFrame, textvariable=chosenDict, width=20)
        self.dictCB['values'] = [m for m in ARUCO_DICT]
        self.dictCB['state'] = 'readonly'
        self.dictCB.grid(column=1, row=1, ipadx=10)

        Label(master=self.mainDisplayFrame, text='Please enter the ID of the tag(1, 2, 3, 4, ... etc.):', pady=50,font=self.txtBodyFormatting, justify='left').grid(column=0, row=2)

        self.arucoTagIDText = Entry(master=self.mainDisplayFrame, width = 10)
        self.arucoTagIDText.grid(column=1, row=2)
        
        Label(master=self.mainDisplayFrame, text='Please enter the size of the tag:', pady=50,font=self.txtBodyFormatting).grid(column=0, row=3)

        self.arucoTagSizeText = Entry(master=self.mainDisplayFrame, width = 10)
        self.arucoTagSizeText.grid(column=1, row=3)

        Button(master=self.mainDisplayFrame, text="Generate Tag", activebackground="gray99", activeforeground="gray50", font=self.txtBodyFormatting, command=self.generate_params ).grid(column=2, row=4, padx=20)
    
    def draw_detect(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="sienna1")
        self.mainDisplayFrame.pack()




        


       


gui = Gui()
#gui.home()
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

    navbarOptions = {"home":"Home", "generate" : "Generate Markers", "calibrate" : "Calibrate", "detect" : "Detect Pose"}

    txtBodyFormatting = 'TkDefaultFont 16'
    txtHeadingFormatting = 'TkDefaultFont 18 bold'


    def __init__(self):
        self.state = self.navbarOptions["home"]
        self.window = Tk()
        self.window.geometry("1200x800+0+0")
        #self.window.after(33,self.update)
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
import numpy as np
import cv2 as cv
import os
import argparse
from   tkinter import *
import tkinter as tk

class Gui:

    welcomeMessage = "Hi! welcome to group fourexplore's pose detection system read below to get started."
    genTagsMessage = "Generate tags will create a file which you can use to print out a tag, using this tag in the next stages will enable you to estimate the pose of the tag in 3D space!"
    calibrateMessage = "This tab allows for our program to get a better understand of where your tag is in space, calibrating the camera is a necessary phase before you can continue to Detect Pose."
    detectPoseMessage = "This tab will use the camera to tell you just where the tag is in 3D space."

    navbarOptions = {"home":"Home", "generate" : "Generate Markers", "calibrate" : "Calibrate", "detect" : "Detect Pose"}

    def __init__(self):
        self.state = self.navbarOptions["home"]
        self.window = tk.Tk()
        self.window.geometry("1200x800+0+0")
        self.gui_navbar()
        self.draw_home()
        self.window.mainloop()
    
    def draw(self, tab):
        if (self.state == 'home'):
            self.homeFrame.forget()
            self.homeFrame.destroy()
        if (self.state == 'generate'):
            self.generateFrame.forget()
            self.generateFrame.destroy()


        if(tab == 'home'):
            self.draw_home()
        if(tab == 'generate'):
            self.draw_generate()
        if (tab == 'calibrate'):
            self.draw_calibrate()
        if (tab == 'detect'):
            self.draw_detect()

    def gui_navbar(self):
        topFrame = tk.Frame(
            master = self.window,
            bg = "white")
        topFrame.pack(
            side = "top",
            fill = tk.X)
        for x in self.navbarOptions:
            tk.Button(topFrame, text=self.navbarOptions[x], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command=self.draw(x) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)


    def draw_home(self):
        self.homeFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="gray50")
        self.homeFrame.pack(side="top")
        tk.Label(master=self.homeFrame, text=self.welcomeMessage, pady=50).pack()
        tk.Label(master=self.homeFrame, text=self.genTagsMessage, pady=50).pack()
        tk.Label(master=self.homeFrame, text=self.calibrateMessage, pady=50).pack()
        tk.Label(master=self.homeFrame, text=self.detectPoseMessage, pady=50).pack()

    def draw_generate(self):
        self.generateFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="medium orchid")

    def draw_calibrate(self):
        self.calibrateFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="dark olive green")
    
    def draw_detect(self):
        self.detectFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="sienna1")



        


       


gui = Gui()
#gui.home()
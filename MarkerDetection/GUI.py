from ast import Lambda
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
        topFrame = tk.Frame(
            master = self.window,
            bg = "white")
        topFrame.pack(
            side = "top",
            fill = tk.X)
        tk.Button(topFrame, text=self.navbarOptions["home"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["home"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        tk.Button(topFrame, text=self.navbarOptions["generate"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["generate"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        tk.Button(topFrame, text=self.navbarOptions["calibrate"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["calibrate"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)
        tk.Button(topFrame, text=self.navbarOptions["detect"], bg="gray85", fg="gray1", activebackground="gray99", activeforeground="gray50", command= lambda: self.draw(self.navbarOptions["detect"]) ).pack(side="left", fill=tk.X, ipadx=30, ipady=30, expand=True)

    def draw_home(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,)
        self.mainDisplayFrame.pack(side="top")
        tk.Label(master=self.mainDisplayFrame, text=self.welcomeMessage, pady=10, padx=0).pack(anchor=tk.W, ipadx=0)
        tk.Label(master=self.mainDisplayFrame, text=self.navbarOptions["generate"],font='TkDefaultFont 18 bold').pack(anchor=tk.W)
        tk.Label(master=self.mainDisplayFrame, text=self.genTagsMessage, pady=10).pack(anchor=tk.W)
        tk.Label(master=self.mainDisplayFrame, text=self.calibrateMessage, pady=10).pack(anchor=tk.W)
        tk.Label(master=self.mainDisplayFrame, text=self.detectPoseMessage, pady=10).pack(anchor=tk.W)

    def draw_generate(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="medium orchid")
        self.mainDisplayFrame.pack()

    def draw_calibrate(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="dark olive green")
        self.mainDisplayFrame.pack()
    
    def draw_detect(self):
        self.mainDisplayFrame = tk.Frame(
            master=self.window,
            width = 1200,
            height= 800,
            bg="sienna1")
        self.mainDisplayFrame.pack()

    #def update(self):
    #    self.window.after(33,self.update)
    #    self.window.update()



        


       


gui = Gui()
#gui.home()
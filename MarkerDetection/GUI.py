import numpy as np
import cv2 as cv
import os
import argparse
import tkinter as tk
from   tkinter import filedialog

class Gui:

    display = {"home"}
    
    #def __init__(self):
        

    def home(self):
        self.state = "home"
        window = tk.Tk()
        greeting = tk.Label(
            text="Choose an option",
            background="dark slate grey"
        )
        greeting.pack()
        window.mainloop()


gui = Gui()
gui.home()
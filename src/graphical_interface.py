__author__ = 'Strahinja'


from Tkinter import *
from tkFileDialog import askopenfilename
import analytics
import ctypes  # An included library with Python install.

master = Tk()

 # show an "Open" dialog box and return the path to the selected file
 # returns a path

def show_start_screen(filename):
    if filename == None:
        Tk().withdraw()
        filename = askopenfilename()
        return filename
    else:
        return filename

def open_keyword_list():
    # add an input field
    e = Entry(master)
    e.pack()
    # add a label
    w = Label(master, text = "Enter the words you want to search for (separate with commas): ")
    w.pack()
    # add buttons
    b = Button(master, text = "Analyze", width = 10, command = analytics.callback(e.get(), show_start_screen()))
    exp = Button(master, text = "Export-PDF", width = 10, command =
    b.pack()
    exp.pack()


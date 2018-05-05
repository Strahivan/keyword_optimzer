__author__ = 'Strahinja'

# read in the .doc export from google drive and convert it to a txt-file

from Tkinter import *
import textract
from tkFileDialog import askopenfilename

Tk().withdraw()
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# progress the given file
#text = textract.process(filename, encoding='utf-8')

# open window for input
master = Tk()
e = Entry(master)
e.pack()
w = Label(master, text = "Enter the words you want to search for (separate with commas): ")
w.pack()

def callback():
    searchterms = e.get() # entered terms raw
    search = [word.strip() for word in searchterms.lower().split(",")]
    count = dict.fromkeys(search, 0)

    with open(filename, 'r') as f:
        for line in f:
            for word in line.lower().split("."):
                if word in count:
                # found a word you wanted to count, so count it
                    count[word] += 1
    print (count)

                # found a word you wanted to count, so count it


def export_results():
    with open('results.txt', 'w') as new_results:
        new_results.write('This is a new Export!')

b = Button(master, text = "Analyze", width = 10, command = callback)
exp = Button(master, text = "Export-PDF", width = 10, command = export_results)

b.pack()
exp.pack()
mainloop()



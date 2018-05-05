__author__ = 'Strahinja'
# encoding=utf8

# read in the .doc export from google drive and convert it to a txt-file

from Tkinter import *
import textract
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from tkFileDialog import askopenfilename


import sys
reload(sys)
sys.setdefaultencoding('utf8')

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
    countterm = dict.fromkeys(search, 0)



    file_content = open(filename).read()
    #decodedfile = file_content.decode("utf-8")
    token = sent_tokenize(file_content)
    for sentences in token:
        for terms in countterm:
            if terms in sentences:
                countterm[terms]+=1

    print(countterm)

    #if countterm[i] in token:
     #       countterm[words] += 1
     #       i += 1
     #   else:
     #       print "hello"
     #       i += 1
    #print(countterm)

def export_results():
    with open('results.txt', 'w') as new_results:
        new_results.write('This is a new Export!')

b = Button(master, text = "Analyze", width = 10, command = callback)
exp = Button(master, text = "Export-PDF", width = 10, command = export_results)

b.pack()
exp.pack()
mainloop()



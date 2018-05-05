__author__ = 'Strahinja'

from Tkinter import *
from fpdf import FPDF
import textract
import nltk
from nltk.tokenize import sent_tokenize, word_tokenize
from tkFileDialog import askopenfilename

# show an "Open" dialog box and return the path to the selected file
Tk().withdraw()
filename = askopenfilename()


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

def export_results():
    pdfexp = FPDF()
    pdfexp.add_page()
    pdfexp.set_font("Arial", size=12)
    pdfexp.cell(200, 10, txt="Welcome to Python!", align="C")
    pdfexp.output("results_keyword_analysis.pdf")

b = Button(master, text = "Analyze", width = 10, command = callback)
exp = Button(master, text = "Export-PDF", width = 10, command = export_results)

b.pack()
exp.pack()
mainloop()



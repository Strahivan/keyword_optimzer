__author__ = 'Strahinja'

from Tkinter import *
from fpdf import FPDF
import nltk
import re
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from tkFileDialog import askopenfilename

# maybe important for standarization, not relevant now
APPOSTROPHES = {"'s":"is", "'re":"are", "'m":"am", "'t":"not", "'ll":"will", "ill":"I will", "im":"I am",
                "wanna":"want to", "gonna": "going to"}

# show an "Open" dialog box and return the path to the selected file
Tk().withdraw()
filename = askopenfilename()
stopwordparam = "english"

# open window for input
master = Tk()
mainframe = Frame(master)
mainframe.grid(column=0,row=0, sticky=(N,W,E,S) )
mainframe.columnconfigure(0, weight = 1)
mainframe.rowconfigure(0, weight = 1)
mainframe.pack(pady = 100, padx = 100)

e = Entry(master, width=80)
master.title("Keyword Optimizer")
master.geometry("500x500")
e.pack()
w = Label(master, text = "Enter the words you want to search for (separate with commas): ")
w.pack()

# Create a Tkinter variable
tkvar = StringVar(master)

# Dictionary with options
choices = { 'english','german'}
tkvar.set('english') # set the default option

popupMenu = OptionMenu(mainframe, tkvar, *choices)
Label(mainframe, text="Choose a language").grid(row = 1, column = 1)
popupMenu.grid(row = 2, column =1)

# on change dropdown value
def change_dropdown(*args):
    stopwordparam = tkvar.get()


def callback():

    # handle search terms
    searchterms = e.get()
    stopwordparam = tkvar.get()

    # divide them according to ','
    search = [word.strip() for word in searchterms.lower().split(",")]
    countterm = dict.fromkeys(search, 0)

    # read file
    file_content = open(filename).read().lower()
   # file_content = file_content.encode('utf-8')

    # tokenize file (sentences)
    token = sent_tokenize(file_content)

    cleanedtoken = []
    fill = dict.fromkeys(stopwords.words(stopwordparam), 0)
    for fillword in fill:
        fillword = fillword.encode('utf-8')

    # remove special chars
    for single_word in token:
        single_token = re.split('[,.!?:\n]', single_word)
        single_token = " ".join(single_token)
        cleanedtoken.append(single_token)

    # check cleaned tokens for search terms
    for sentences in cleanedtoken:
        for terms in countterm:
            if terms in sentences:
                numberofkeywords = sentences.count(terms)
                countterm[terms] = countterm[terms]+ numberofkeywords


    # check each stopword single

    for eachsentence in cleanedtoken:
        for eachword in fill:
            if eachword in eachsentence:
                numberofstopwords = eachsentence.count(eachword)
                fill[eachword] = fill[eachword]+ numberofstopwords


    # output of results

    print("\n")
    print("Keyword Analysis: \n")
    for term in countterm:
        print(str(term) + " " + str(countterm[term]) + "\n")

    print("\n")
    print("Stopword Analysis: \n")
    for stopword in fill:
        print(str(stopword.encode('utf-8')) + " " + str(fill[stopword]) + "\n")


def export_results():
    pdfexp = FPDF()
    pdfexp.add_page()
    pdfexp.set_font("Arial", size=12)
    pdfexp.cell(0, 10, txt="Keyword Analysis of file: " + filename, align="C")

    # open file again and standardize it
    file_content = open(filename).read()
    file_content = file_content.lower()
    file_content = file_content.decode("unicode_escape").encode('utf-8')
    stopwordparam = tkvar.get()

    #remove special chars
    oken = word_tokenize(file_content.format())

    nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
    filtered = [w for w in oken if nonPunct.match(w)]

    filtered = [APPOSTROPHES[word] if word in APPOSTROPHES else word for word in filtered]

    number_of_total_words = len(filtered)

    cleanedwords = ' '.join([word for word in filtered if word not in stopwords.words(stopwordparam)])
    cleanedwords = word_tokenize(cleanedwords)


    number_of_stopwords = number_of_total_words - len(cleanedwords)

    print("Total Words " + str(number_of_total_words))
    print("Stopwords " + str(number_of_stopwords))
    print("Clean_Content: " + str(len(cleanedwords)))
    print(stopwordparam)

    # positions need to be fixed
    pdfexp.cell(50, 20, txt="Total Amount of words: "+ str(number_of_total_words), ln = 1, align="C")
    pdfexp.cell(50, 20, txt="Total Amount of Stopwords: "+ str(number_of_stopwords),ln = 1, align="C")
    pdfexp.cell(50, 20, txt="Clean_Content: "+ str(len(cleanedwords)), ln = 1, align="C")


    pdfexp.output("results_keyword_analysis.pdf")

b = Button(master, text = "Analyze", width = 10, command = callback)
exp = Button(master, text = "Export-PDF", width = 10, command = export_results)

b.pack()
exp.pack()
mainloop()



__author__ = 'Strahinja'

from Tkinter import *
from fpdf import FPDF
import textract
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import sent_tokenize, word_tokenize
from tkFileDialog import askopenfilename

# maybe important for standarization, not relevant now
APPOSTROPHES = {"'s":"is", "'re":"are", "'m":"am", "'t":"not", "'ll":"will", "ill":"I will", "im":"I am",
                "wanna":"want to", "gonna": "going to"}

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
    number_of_words = len(token)
    for sentences in token:
        for terms in countterm:
            if terms in sentences:
                countterm[terms]+=1
    print(countterm)

def export_results(Name_of_File):
    pdfexp = FPDF()
    pdfexp.add_page()
    pdfexp.set_font("Arial", size=12)
    pdfexp.cell(0, 10, txt="Keyword Analysis of file: " + Name_of_File, align="C")

    # open file again and standardize it
    file_content = open(Name_of_File).read()
    file_content = file_content.lower()

    #remove special chars
    oken = word_tokenize(file_content)

    nonPunct = re.compile('.*[A-Za-z0-9].*')  # must contain a letter or digit
    filtered = [w for w in oken if nonPunct.match(w)]

    filtered = [APPOSTROPHES[word] if word in APPOSTROPHES else word for word in filtered]

    number_of_total_words = len(filtered)

    cleanedwords = ' '.join([word for word in filtered if word not in stopwords.words("english")])
    cleanedwords = word_tokenize(cleanedwords)


    number_of_stopwords = number_of_total_words - len(cleanedwords)

    print("Total Words " + str(number_of_total_words))
    print("Stopwords " + str(number_of_stopwords))
    print("Clean_Content: " + str(len(cleanedwords)))


    # positions need to be fixed
    pdfexp.cell(10, 0, txt="Total Amount of words: "+ str(number_of_total_words), align="C")
    pdfexp.cell(20, 0, txt="Total Amount of Stopwords: "+ str(number_of_stopwords), align="C")
    pdfexp.cell(30, 0, txt="Clean_Content: "+ str(len(cleanedwords)), align="C")


    pdfexp.output("results_keyword_analysis.pdf")

b = Button(master, text = "Analyze", width = 10, command = callback)
exp = Button(master, text = "Export-PDF", width = 10, command = export_results(filename))

b.pack()
exp.pack()
mainloop()



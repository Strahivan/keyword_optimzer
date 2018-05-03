__author__ = 'Strahinja'

# read in the .doc export from google drive and convert it to a txt-file

from Tkinter import Tk
import textract
from tkFileDialog import askopenfilename

Tk().withdraw() # we don't want a full GUI, so keep the root window from appearing
filename = askopenfilename() # show an "Open" dialog box and return the path to the selected file

# Parse dann die .doc zu einem txt
# lass dann die Keyword counter durchlaufen

#poem = open(filename).readlines()
text = textract.process(filename, encoding='iso-8859-15')
print(text)
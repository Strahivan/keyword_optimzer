__author__ = 'Strahinja'

import nltk
from nltk.tokenize import sent_tokenize, word_tokenize



def callback(keywords, filename):
    search = [word.strip() for word in keywords.lower().split(",")]
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
    with open('results.txt', 'w') as new_results:
        new_results.write()



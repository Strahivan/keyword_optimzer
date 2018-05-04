Windows use: C:\Python27\python.exe <Name_of_py> and C:\Python27\Scripts\pip.exe <pip_command>

cmd: dir - shows list of folders and files in actual path
cmd: cls - clears screen

Hard Requirements so far:
- Python 2.7
- virtualenv

How to activate your virtualenv?
cd into ENV\Scripts and run activate.exe

How to save changes in your virtualenv?
pip freeze > requirements.txt

Use:
- Copy content out of .doc-download into a .txt-file
- .doc-file dosn't work properly


Bugs:
- look at textract.process (filename, encoding) what's the return of this method? Maybe this causes errors?
- mainloop() has to stop
- encoding bug for german umlauts
- create export button with export functionality (PDF-export)
- Stopwords have to be checked
- Language (German/English)
- Issue with whitespaces in keywords - add smth. like '\n' ?
- If i click on red "X" the program should stop running (Close)
- Close the file you opened after analyzing

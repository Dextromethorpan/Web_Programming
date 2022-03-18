import datetime
import os
os.getcwd()

class LMS:
    """This class is used to keep record of books library.
       It has total four module: "Display Books","Issue Books", "Return Books","Add Books" """
    
    def __init__(self,list_of_books,library_name):
        self.list_of_books="list_of_books.tex"
        self.library_name=library_name
        self.books_dict={}
        Id=101
        with open(self.list_of_books) as bk:
            content=bk.readline()
        
        for line in content:
            self.books_dict.update()
            #print(line)

print(LMS("list_of_books.tex","Python's Library"))


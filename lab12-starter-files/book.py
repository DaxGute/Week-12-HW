class Book(object):
    """ class for a single Book object """

    def __init__(self, title, author, year, filename):
        self.title = title
        self.author = author 
        self.year = year 
        self.filename = filename 
        self.bookmark = 0
        

    def toString(self):
        """ pretty-print info about this object """
        printStringFormat = "{bookName:>25} by {authorDate:>20}"
        bookName = "" + self.title
        authorDate = "" + self.author + " (" + str(self.year) + ")"
        return printStringFormat.format(bookName=bookName, authorDate=authorDate)
        
    def getFilename(self):
        return self.filename

    def getText(self):
        infile = open(self.getFilename(), "r")
        text = ""
        for line in infile:
            if line[0] != "#":
                text += line
        infile.close()
        return text

    def getTitle(self):
        return self.title

    def getAuthor(self):
        return self.author

    def getYear(self):
        return self.year

    def getBookmark(self):
        return self.bookmark

    def setBookmark(self, pageNum):
        self.bookmark = pageNum

    

    
    ###  METHODS TO BE COMPLETED BY YOU  ###



if __name__ == '__main__':

    print("Testing the Book class...")
    myBook = Book("Gettysburg Address", "Abe Lincoln", 1863,
    "book-database/gettysburg.txt")

    print("Testing toString...")
    print(myBook.toString())

    print("Testing getFilename...")
    print(myBook.getFilename())

    print("Testing getText...")
    text = myBook.getText()
    print(text[:105])                   # only print the first couple of lines

    print("bookmark is:", myBook.getBookmark())
    myBook.setBookmark(12)
    print("now bookmark is:", myBook.getBookmark())

    ################ Write additional tests below ###################

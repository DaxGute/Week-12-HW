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
        printStringFormat = "{bookName:>25} by {authorDate:>27}"
        bookName = "" + self.title
        authorDate = "" + self.author + " (" + str(self.year) + ")"
        return printStringFormat.format(bookName=bookName, authorDate=authorDate)


    def __str__(self):
        """ info about this object for the programmer """
        print("Title: " + self.title)
        print("Author: " + self.author)
        print("Year " + self.year)
        print("Author: " + self.filename)
        print("Title: " + self.bookmark)


    def getFilename(self):
        """ returns the filename of this book """
        return self.filename

    def getText(self):
        """ returns the text of the filename of this book """
        infile = open(self.getFilename(), "r")
        text = ""
        for line in infile:
            if line[0] != "#":
                text += line
        infile.close()
        return text

    def getTitle(self):
        """ returns the title of this book """
        return self.title

    def getAuthor(self):
        """ returns the author of this book """
        return self.author

    def getYear(self):
        """ returns the year of this book """
        return self.year

    def getBookmark(self):
        """ returns the bookmark of this book """
        return self.bookmark

    def setBookmark(self, pageNum):
        """ sets the bookmark of the book at the page number that is passed in"""
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

    #additional tests added below
    print("Testing getTitle...")
    print(myBook.getTitle())
    print("Testing getAuthor...")
    print(myBook.getAuthor())
    print("Testing getYear...")
    print(myBook.getYear())
    print("Testing getBookmark...")
    print(myBook.getBookmark())

    print("Testing getText...")
    text = myBook.getText()
    print(text[:105])                   # only print the first couple of lines

    print("bookmark is:", myBook.getBookmark())
    myBook.setBookmark(12)
    print("now bookmark is:", myBook.getBookmark())
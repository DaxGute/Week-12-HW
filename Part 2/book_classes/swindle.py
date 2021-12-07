from .book import *

def readBookDatabase(filename):
    """ read in book info from bookdb.txt, save each line as a Book object in list.
        This list will be returned and will serve as availableBooks. """
    infile = open(filename, 'r')
    availableBooks = []
    for book in infile:
        bookInfo = book.strip()
        bookInfoArray = bookInfo.split(",")
        newBook = Book(bookInfoArray[0], bookInfoArray[1], bookInfoArray[2], bookInfoArray[3])
        availableBooks.append(newBook)

    return availableBooks


class Swindle(object):
    """ class for a single Swindle object """

    def __init__(self, owner):
        """ constructor for swindle object, given ________________________ """
        self.availableBooks = readBookDatabase("bookdb.txt")    # list of Book objects
        self.owner = owner
        self.ownedBooks = []
        self.pageLength = 30

    def __str__(self):
        """ pretty-print info about this object """
        ###  TO BE COMPLETED BY YOU  ###
        s = ""
        return s

    def getPage(self, book):
        """ This method displays a single page at a time (300 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        pageText = ""
        for i in range(pageStart, pageEnd):
            pageText += bookLinesList[i] + " "
        pageWords = pageText.split(" ")
        arbitraryScalarForThisVariable = self.pageLength + (30 - self.pageLength)/4
        perLine = len(pageText) / arbitraryScalarForThisVariable
        pageLines = []
        currentLine = ""
        for word in pageWords:
            if len(currentLine) > perLine:
                pageLines.append(currentLine)
                currentLine = word + " "
            else:
                currentLine += word + " "
            
        return pageLines

    def displayText(self, book):
        """ This method allows the user to read one of their books.
            It calls displayPage() to show a single page at a time.
            It calls getLetter() to determine what the user wants to do next.
            When the user decides to quit reading a particular book, this method
            returns the (updated) Book object.
        """
        while True:
            self.displayPage(book)
            currentPage = book.getBookmark()
            choice = self.getLetter()       # user chooses to quit or read the next/previous page
            if choice == "q":               # quit reading and return to ereader
                return book
            elif choice == "n":                 # move on to the next page in the book
                bookContents = book.getText()   # unless user is on the last page
                numLines = bookContents.count("\n")
                currentLine = currentPage * self.pageLength
                if (currentLine + 1) < (numLines - self.pageLength):
                    book.setBookmark(currentPage+1)
                else:
                    print("\nThere are no more pages. Enter 'p' to go to the previous page or 'q' to quit.")
            else:                               # return to previous page in the book
                book.setBookmark(currentPage-1)
        return

    def buy(self, intChoice):
        """ after viewing from all available books to purchase, the user can choose to purchase
        one of the selection or (by typing 0) none of the selection. """
        if intChoice != 0:
            newBook = self.availableBooks.pop(intChoice-1)
            self.ownedBooks.append(newBook)

    def getOwner(self):
        """ returns the owner of the swindle """
        return self.owner


if __name__ == '__main__':
    print("Testing the Swindle class...")
    owner = "Lionel"
    myswindle = Swindle(owner)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    print("Buying a book...")
    myswindle.ownedBooks.append(myswindle.availableBooks[2])
    myswindle.availableBooks.pop(2)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    print("Buying another book...")
    myswindle.ownedBooks.append(myswindle.availableBooks[2])
    myswindle.availableBooks.pop(2)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    ################ Write additional tests below ###################

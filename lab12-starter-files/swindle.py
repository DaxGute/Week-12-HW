from book import *


def readBookDatabase(filename):
    """ read in book info from bookdb.txt, save each line as a Book object in list.
        This list will be returned and will serve as availableBooks. """
    infile = open(filename, 'r')
    availableBooks = []
    for bookInfo in infile:
        # TODO: read in book info (title, author, year published)
        bookInfoArray = ["", "", "", ""]
        currentInfoIndex = 0
        for char in bookInfo:
            if char != ",":
                bookInfoArray[currentInfoIndex] += char
            else:
                currentInfoIndex += 1

        newBook = Book(bookInfoArray[0], bookInfoArray[1], bookInfoArray[2], bookInfoArray[3])
        availableBooks.append(newBook)

    return availableBooks
        # TODO: using the information just obtained from the file, create a
        # Book object with this data and add it to the availableBooks list


class Swindle(object):
    """ class for a single Swindle object """

    def __init__(self, owner):
        """ constructor for swindle object, given ________________________ """
        self.availableBooks = readBookDatabase("bookdb.txt")    # list of Book objects
        self.owner = owner
        self.ownedBooks = []
        self.pageLength = 20

    def __str__(self):
        """ pretty-print info about this object """
        ###  TO BE COMPLETED BY YOU  ###
        s = ""
        return s

    def getLetter(self):
        """ This method determines what the user wants to do next """
        validChoices = ['n', 'p', 'q']
        while True:
            readingChoice = str(input("\nn (next); p (previous); q (quit): "))
            if readingChoice in validChoices:
                return readingChoice
            print("invalid input, try again")

    def displayPage(self, book):
        """ This method displays a single page at a time (300 chars) """
        bookContents = book.getText()
        bookLinesList = bookContents.split("\n")
        numLines = len(bookLinesList)
        numPages = numLines // self.pageLength  # calculate total number of pages in book
        page = book.getBookmark()               # get current page (most recently read)
        pageStart = page * self.pageLength
        pageEnd = pageStart + self.pageLength   # display 20 lines per page
        if pageEnd > numLines:
            pageEnd = numLines                  # in case you're at the end of the book
        for i in range(pageStart, pageEnd):
            print(bookLinesList[i])
        if numPages == 1:                       # alter page numbers for 1-page books
            page = 1
        print("\nShowing page %d out of %d" % (page, numPages))
        return

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


    def buy(self):
        self.showAvailable()
        bookInputInvalid = True 
        while (bookInputInvalid):
            try:
                intChoice = int(input("Which book would you like to buy? (0 to skip): "))
                if (0 <= intChoice <= len(self.availableBooks)): 
                    bookInputInvalid = False
                else: 
                    print("invalid input, try again")
            except:
                print("invalid input, try again")

        if intChoice != 0:
            self.ownedBooks.append(self.availableBooks[intChoice-1])
            print("\nYou've successfully purchased the book: " + self.availableBooks[intChoice-1].getTitle())


            
        

    def showOwned(self):
        for book in self.ownedBooks:
            print(book.toString())

    def showAvailable(self):
        for i in range(len(self.availableBooks)):
            print(str(i + 1) + ") " + self.availableBooks[i].toString())

    def getOwner(self):
        return self.owner


if __name__ == '__main__':
    print("Testing the Swindle class...")
    owner = "Lionel"
    myswindle = Swindle(owner)

    print("Testing showAvailable...")
    myswindle.showAvailable()

    print("Testing showOwned...")
    myswindle.showOwned()

    ################ Write additional tests below ###################

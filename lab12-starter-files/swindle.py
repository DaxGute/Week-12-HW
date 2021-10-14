from book import *


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
            print("")
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

    def getChoice(listOfBook, prompt):
        """ returns the choice of a user after the user chooses an acceptable response"""
        intChoice = -1
        bookInputInvalid = True 
        while (bookInputInvalid):
            choice = input(prompt)
            try:
                intChoice = int(choice)
                if (0 <= intChoice <= len(listOfBook)): 
                    bookInputInvalid = False
                else: 
                    print("invalid input, try again")
            except:
                print("invalid input, try again")

        return intChoice

    def buy(self):
        """ after viewing from all available books to purchase, the user can choose to purchase
        one of the selection or (by typing 0) none of the selection. """
        self.showAvailable()
        print("")
        intChoice = Swindle.getChoice(self.availableBooks, "Which book would you like to buy? (0 to skip): ")
        
        if intChoice != 0:
            self.ownedBooks.append(self.availableBooks[intChoice-1])
            self.availableBooks.pop(intChoice-1)
            print("\nYou've successfully purchased the book: " + self.availableBooks[intChoice-1].getTitle())


    def read(self):
        """ after beening shown a selection of all the books a reader can choose one of the books to read. After choosing that book
        the displayText() method is used to function as the pages. """
        self.showOwned()
        print("")
        intChoice = Swindle.getChoice(self.availableBooks, "Which book would you like to buy? (0 to skip): ")
    
        print("")
        if intChoice != 0:
            readingBook = self.ownedBooks[intChoice-1]
            self.displayText(readingBook)
            print("\nSetting bookmark in " + readingBook.title + " at page " + str(readingBook.getBookmark()))
            

    def showOwned(self):
        """ This method shows all of the books that the user owns in a readable format. """
        if len(self.ownedBooks) > 0:
            print("\nBooks you own: ")
            for i in range(len(self.ownedBooks)):
                print(str(i + 1) + ") " + self.ownedBooks[i].toString())
        else:
            print("\nYou don't own any books!")

    def showAvailable(self):
        """ This method shows all the books that are available to purchase in a readable format. """
        print("\nAvailable books: ")
        for i in range(len(self.availableBooks)):
            print(str(i + 1) + ") " + self.availableBooks[i].toString())

    def getOwner(self):
        """ returns the owner of the swindle """
        return self.owner


#TODO check that end of book roll over actually works
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

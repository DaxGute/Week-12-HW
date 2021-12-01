from book_classes.swindle import *
from os.path import isfile
from graphics.rendering import *
from graphics.graphics import *

def newUser():
    print("\nSince this is the first time you used it,")
    print("let's customize your Swindle...")
    owner = str(input("\nPlease enter your name: "))
    print("\nWelcome to %s's Swindle v1.0!" % owner)
    return owner

def loadBook(title, bookmark, userSwindle):
    """ loads a book onto the swindle """
    for i in range(len(userSwindle.availableBooks)):
        book = userSwindle.availableBooks[i]
        if book.getTitle() == title:
            newBook = userSwindle.availableBooks.pop(i)
            newBook.setBookmark(bookmark)
            userSwindle.ownedBooks.append(newBook)
            break

def loadPref(win):
    """ gets the user preferences """
    if isfile("save.txt"):
        infile = open("save.txt", "r")
        lines = []
        for line in infile:
            lines.append(line)
        infile.close()

        username = lines[0].strip()
        welcomeBackMessage(win, username)
        userSwindle = Swindle(username)

        for i in range(1, len(lines)):
            bookDesc = lines[i].split(",")
            title = bookDesc[0]
            bookmark = int(bookDesc[1])

            loadBook(title, bookmark, userSwindle)

        return userSwindle
    else:
        owner = welcomeFirstMessage(win)
        return Swindle(owner)

def savePref(userSwindle):
    """ closes the book and saves the data """
    outfile = open("save.txt", "w")
    outfile.write("%s\n" % userSwindle.owner)
    for book in userSwindle.ownedBooks:
        outfile.write("%s, " % book.getTitle())
        outfile.write("%d \n" % book.getBookmark())
    outfile.close()

def mainMenu():
    print("\n--------------------------------------------------\n")
    print("1) Buy/See available books\n2) See owned books\n3) Read a book\n4) Exit\n")
    while True:
        userInput = str(input("---> "))
        try:
            menuChoice = int(userInput)
            if 1 <= menuChoice <= 4:
                return menuChoice
            else:
                print("invalid number, try again")
        except ValueError:
            print("invalid input, try again")

def main():
    win = GraphWin(width = 500, height = 600) # create a window

    userSwindle = loadPref(win)

    while True:
        menuChoice = displayChoices(win)         # Display ereader's main menu
        if menuChoice == 1:
            userSwindle.buy()           # View available books with option to buy
        elif menuChoice == 2:
            userSwindle.showOwned()     # View owned books
        elif menuChoice == 3:
            userSwindle.read()          # Choose a book to read
        else:
            savePref(userSwindle)       # Turn off ereader (quit the program)
            break 


main()

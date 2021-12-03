from graphics.graphics import *
from graphics.button import Button
def clear(win):
    for item in win.items[:]:
        item.undraw()
    win.update()

def welcomeBackMessage(win, username):
    mainText = Text(Point(win.width/2, win.height/4), "Welcome back")
    mainText.setTextColor("red")
    mainText.setSize(20)
    mainText.draw(win)

    nameText = Text(Point(win.width/2, win.height/3),  "" + username + "!")
    nameText.setTextColor("red")
    nameText.setSize(25)
    nameText.draw(win)

    clickText = Text(Point(win.width/2, win.height - 10),  "[Click Anywhere to Continue]")
    clickText.setTextColor("black")
    clickText.setSize(10)
    clickText.draw(win)

    win.getMouse()

def welcomeFirstMessage(win):
    firstTimeText = Text(Point(win.width/2, win.height/4), "Since this is the first time you used it,")
    firstTimeText.setTextColor("blue")
    firstTimeText.setSize(20)
    firstTimeText.draw(win)

    custText = Text(Point(win.width/2, win.height/4 + 20), "let's customize your Swindle...")
    custText.setTextColor("blue")
    custText.setSize(20)
    custText.draw(win)

    enterText = Text(Point(win.width/2 - 60, win.height/2), "Please enter your name: ")
    enterText.setTextColor("black")
    enterText.setSize(20)
    enterText.draw(win)

    inputBox = Entry(Point(win.width/2 + 120, win.height/2), 10)
    inputBox.draw(win)

    # clickText = Text(Point(win.width/2, win.height/2 + 25),  "[Click Anywhere to Lock In Name]") # TODO: make better
    # clickText.setTextColor("black")
    # clickText.setSize(10)
    # clickText.draw(win)

    confirmButton = Button(Point(win.width/2-100, win.height/2 + 50), Point(win.width/2+100, win.height/2 + 100), "Confirm?", "cyan4", win)

    point = win.getMouse()
    while not confirmButton.checkCollision(point):
        point = win.getMouse()

    ownerName = inputBox.getText()

    firstTimeText.undraw()
    custText.undraw()
    enterText.undraw()
    inputBox.undraw()
    confirmButton.delete()

    welcomeText = Text(Point(win.width/2, win.height/2), "Welcome to %s's Swindle v1.0!" % ownerName)
    welcomeText.setTextColor("blue")
    welcomeText.setSize(30)
    welcomeText.draw(win)

    click2Text = Text(Point(win.width/2, win.height - 10),  "[Click Anywhere to Continue]")
    click2Text.setTextColor("black")
    click2Text.setSize(10)
    click2Text.draw(win)

    win.getMouse()

    return ownerName


def displayChoices(win):
    clear(win)
    buyButton = Button(Point(10, 10), Point(win.width-10, win.height/4 - 5), "Buy/See available books", "cyan4", win)
    ownedButton = Button(Point(10, win.height/4 + 5), Point(win.width-10, win.height/2 - 5), "See owned books", "cyan4", win)
    readButton = Button(Point(10, win.height/2 + 5), Point(win.width-10, 3*win.height/4 - 5), "Read a book", "cyan4", win)
    exitButton = Button(Point(10, 3*win.height/4 + 5), Point(win.width-10, win.height - 10), "Exit", "cyan4", win)

    buttons = [buyButton, ownedButton, readButton, exitButton] 
    while True:
        point = win.getMouse()
        for i in range(4):
            if buttons[i].checkCollision(point):
                buyButton.delete()
                ownedButton.delete()
                readButton.delete()
                exitButton.delete()
                return i + 1

def buyOptions(win, userSwindle):
    clear(win)
    closeButton = Button(Point(2, 2), Point(25, 25), "X", "red", win)
    prevPage = Button(Point(2, win.height - 25), Point(30, win.height - 2), "<--", "red2", win)
    nextPage = Button(Point(win.width - 30, win.height - 25), Point(win.width - 2, win.height - 2), "-->", "red2", win)

    allBooks = userSwindle.availableBooks
    pageNum = 0
    pageBooks = []
    while True:
        firstBook = allBooks[(pageNum*4)]
        firstButton = Button(Point(50, 50), Point(win.width-50, 170), firstBook.toString(), "DarkOrchid4", win)
        pageBooks.append(firstButton)
        try:
            secondBook = allBooks[(pageNum*4)+1]
            secondButton = Button(Point(50, 175), Point(win.width-50, 295), secondBook.toString(), "DarkOrchid4", win)
            pageBooks.append(secondButton)
        except:
            secondBook = None
        try:
            thirdBook = allBooks[(pageNum*4)+2]
            thirdButton = Button(Point(50, 300), Point(win.width-50, 420), thirdBook.toString(), "DarkOrchid4", win)
            pageBooks.append(thirdButton)
        except:
            thirdBook = None
        try: 
            forthBook = allBooks[(pageNum*4)+3]
            forthButton = Button(Point(50, 425), Point(win.width-50, 545), forthBook.toString(), "DarkOrchid4", win)
            pageBooks.append(forthButton)
        except:
            forthBook = None
        
        point = win.getMouse()

        if closeButton.checkCollision(point):
            return
        elif nextPage.checkCollision(point):
            if pageNum < len(allBooks)/4 - 1:
                pageNum += 1
                for bookButton in pageBooks:
                    bookButton.delete()
                pageBooks = []
        elif prevPage.checkCollision(point):
            if pageNum > 0:
                pageNum -= 1
                for bookButton in pageBooks: #clear current buttons
                    bookButton.delete()
                pageBooks = []
        else:
            for i in range(len(pageBooks)):
                if pageBooks[i].checkCollision(point):
                    userSwindle.buy(pageNum*4 + i + 1)
                    return 

def showOwned(win, userSwindle):
    clear(win)
    closeButton = Button(Point(2, 2), Point(25, 25), "X", "red", win)
    if len(userSwindle.ownedBooks) < 0:
        mainText = Text(Point(win.width/2, win.height/2), "You don't own any books")
        mainText.setSize(30)
        mainText.draw(win)
    else:
        mainText = Text(Point(win.width/2, 100), "Books you own:")
        mainText.setSize(30)
        mainText.draw(win)
        for i in range(len(userSwindle.ownedBooks)):
            listIndex = Text(Point(win.width/2 - 150, 140 + (i*20)), str(i+1) + ")")
            listIndex.draw(win)
            book = userSwindle.ownedBooks[i]
            bookList = Text(Point(win.width/2, 140 + (i*20)), book.toString())
            bookList.draw(win)
    
    while True:
        point = win.getMouse()      
        if closeButton.checkCollision(point):
            return

def readOptions(win, userSwindle):
    clear(win)
    closeButton = Button(Point(2, 2), Point(25, 25), "X", "red", win)
    prevPage = Button(Point(2, win.height - 25), Point(30, win.height - 2), "<--", "red2", win)
    nextPage = Button(Point(win.width - 30, win.height - 25), Point(win.width - 2, win.height - 2), "-->", "red2", win)

    allBooks = userSwindle.ownedBooks
    pageNum = 0
    pageBooks = []
    while True:
        firstBook = allBooks[(pageNum*4)]
        firstButton = Button(Point(50, 50), Point(win.width-50, 170), firstBook.toString(), "plum1", win)
        pageBooks.append(firstButton)
        try:
            secondBook = allBooks[(pageNum*4)+1]
            secondButton = Button(Point(50, 175), Point(win.width-50, 295), secondBook.toString(), "plum1", win)
            pageBooks.append(secondButton)
        except:
            secondBook = None
        try:
            thirdBook = allBooks[(pageNum*4)+2]
            thirdButton = Button(Point(50, 300), Point(win.width-50, 420), thirdBook.toString(), "plum1", win)
            pageBooks.append(thirdButton)
        except:
            thirdBook = None
        try: 
            forthBook = allBooks[(pageNum*4)+3]
            forthButton = Button(Point(50, 425), Point(win.width-50, 545), forthBook.toString(), "plum1", win)
            pageBooks.append(forthButton)
        except:
            forthBook = None
        
        point = win.getMouse()

        if closeButton.checkCollision(point):
            return
        elif nextPage.checkCollision(point):
            if pageNum < len(allBooks)/4 - 1:
                pageNum += 1
                for bookButton in pageBooks:
                    bookButton.delete()
                pageBooks = []
        elif prevPage.checkCollision(point):
            if pageNum > 0:
                pageNum -= 1
                for bookButton in pageBooks: #clear current buttons
                    bookButton.delete()
                pageBooks = []
        else:
            for i in range(len(pageBooks)):
                if pageBooks[i].checkCollision(point):
                    book = userSwindle.ownedBooks[pageNum*4 + i]
                    readBook(win, book, userSwindle)
                    return 

def readBook(win, book, userSwindle):
    clear(win)
    closeButton = Button(Point(2, 2), Point(25, 25), "X", "red", win)
    prevPage = Button(Point(2, win.height - 25), Point(30, win.height - 2), "<--", "red2", win)
    nextPage = Button(Point(win.width - 30, win.height - 25), Point(win.width - 2, win.height - 2), "-->", "red2", win)
    increaseFont = Button(Point(win.width - 30, win.height/2 - 30), Point(win.width - 2, win.height/2 - 2), "+", "lightSalmon", win)
    decreaseFont = Button(Point(win.width - 30, win.height/2 + 2), Point(win.width - 2, win.height/2 + 30), "-", "lightSalmon", win)

    fontSize = 15
    lineSpace = 17
    canDraw = True
    pageLines = userSwindle.getPage(book)
    pageText = []
    while True:

        if canDraw:
            pageLines = userSwindle.getPage(book)
            pageText = []
            for i in range(len(pageLines)):
                vertSpacing = 70 + (7*(fontSize - 15)) + (i*(lineSpace))
                lineText = Text(Point(win.width/2, vertSpacing), pageLines[i])
                lineText.setSize(fontSize)
                lineText.draw(win)
                pageText.append(lineText)

        canDraw = True
        point = win.getMouse()      
        if closeButton.checkCollision(point):
            return
        elif nextPage.checkCollision(point):
            book.bookmark += 1
            for pageLine in pageText:
                pageLine.undraw()
        elif prevPage.checkCollision(point):
            book.bookmark -= 1
            for pageLine in pageText:
                pageLine.undraw()
        elif increaseFont.checkCollision(point):
            if fontSize < 18:
                userSwindle.pageLength -= 4
                lineSpace += 1.5
                fontSize += 1
            for pageLine in pageText:
                pageLine.undraw()

        elif decreaseFont.checkCollision(point):
            if fontSize > 12:
                userSwindle.pageLength += 4
                lineSpace -= 1.5
                fontSize -= 1
            for pageLine in pageText:
                pageLine.undraw()
            
        else:
            canDraw = False

    
    
        


    

    



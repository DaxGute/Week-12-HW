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
        for i in range in len(4):
            if buttons[i].checkCollision(point):
                buyButton.delete()
                ownedButton.delete()
                readButton.delete()
                exitButton.delete()
                return i

def buyOptions(win, userSwindle):
    clear(win)
    closeButton = Button(Point(2, 2), Point(10, 10), "X", "red", win)
    prevPage = Button(Point(2, win.height - 10), Point(15, win.height - 2), "<--", "red2", win)
    nextPage = Button(Point(win.width - 15, win.height - 10), Point(win.width - 2, win.height - 2), "-->", "red2", win)

    allBooks = userSwindle.availableBooks
    pageNum = 0
    while True:
        point = win.getMouse()
        pageBooks = []
        firstBook = allBooks[(pageNum*4)]
        firstButton = Button(Point(50, 50), Point(win.width-50, win.height/4 - 5), firstBook.toString(), "DarkOrchid4", win)
        pageBooks.append(firstButton)
        try:
            secondBook = allBooks[(pageNum*4)+1]
            secondButton = Button(Point(50, win.height/4 + 5), Point(win.width-50, win.height/2 - 5), secondBook.toString(), "DarkOrchid4", win)
            pageBooks.append(secondButton)
        except:
            secondBook = None
        try:
            thirdBook = allBooks[(pageNum*4)+2]
            thirdButton = Button(Point(50, win.height/2 + 5), Point(win.width-50, 3*win.height/4 - 5), thirdBook.toString(), "DarkOrchid4", win)
            pageBooks.append(thirdButton)
        except:
            thirdBook = None
        try: 
            forthBook = allBooks[(pageNum*4)+3]
            pageBooks.append(forthBook)
        except:
            forthBook = None

        


    

    



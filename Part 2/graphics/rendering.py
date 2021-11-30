from graphics.graphics import *

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

    inputText = Entry(Point(win.width/2 + 120, win.height/2), 10)
    inputText.draw(win)

    clickText = Text(Point(win.width/2, win.height/2 + 25),  "[Click Anywhere to Lock In Name]") # TODO: make better
    clickText.setTextColor("black")
    clickText.setSize(10)
    clickText.draw(win)

    win.getMouse()
    ownerName = inputText.getText()

    firstTimeText.undraw()
    custText.undraw()
    enterText.undraw()
    inputText.undraw()
    clickText.undraw()

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


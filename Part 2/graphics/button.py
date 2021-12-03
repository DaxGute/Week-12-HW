from graphics.graphics import *
class Button:

    def __init__(self, p1, p2, text, color, win):
        self.x1 = p1.getX()
        self.y1 = p1.getY()
        self.x2 = p2.getX()
        self.y2 = p2.getY()
        self.color = color
        self.boxRect = Rectangle(Point(self.x1, self.y1), Point(self.x2, self.y2))
        self.boxRect.setFill(color)
        self.boxText = Text(Point(self.x1 + (self.x2 - self.x1)/2, self.y1 + (self.y2 - self.y1)/2), text)
        self.boxRect.draw(win)
        self.boxText.draw(win)


    def delete(self):
        self.boxRect.undraw()
        self.boxText.undraw()

    def checkCollision(self, mousePoint):
        if (self.x1 < mousePoint.getX() < self.x2) and (self.y1 < mousePoint.getY() < self.y2):
            self.boxRect.setFill("gray")
            time.sleep(0.2)
            self.boxRect.setFill(self.color)
            return True
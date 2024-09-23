#TurtleGraphics.py
#Name: Jakob cimino
#Date: 9/22/2024
#Assignment: Lab 4

import turtle #needed generally but not in CodeHS
hideturtle() #hides the default turtle in CodeHS

def drawSquare(myTurtle, size):
    for i in range(4):
        myTurtle.forward(size)
        myTurtle.right(90)

def drawPolygon(tupac, sides):
    for s in range(sides):
        tupac.forward(100)
        tupac.right(360/5)
def drawPolygon(biggiesmalls, sides):
    for s in range(sides):
        biggiesmalls.forward(80)
        biggiesmalls.right(360/8)
        
def fillCorner(scooby, corner):
    drawSquare(scooby, 150)
    if corner == 1:
        scooby.begin_fill()
        drawSquare(scooby, 75)
        scooby.end_fill()
    elif corner == 2:
        scooby.forward(75)
        scooby.begin_fill()
        drawSquare(scooby, 75)
        scooby.end_fill()
    elif corner == 3:
        scooby.right(90)
        scooby.forward(75)
        scooby.left(90)
        scooby.begin_fill()
        drawSquare(scooby, 75)
        scooby.end_fill()

def squaresInSquares(huskers, number):
    if number == 5:
        for i in range(4):
            huskers.forward(50)
            huskers.right(90)
        huskers.penup()
        huskers.goto(-10,10)
        huskers.pendown()
        for i in range(4):
            huskers.forward(70)
            huskers.right(90)
        huskers.penup()
        huskers.goto(-20,20)
        huskers.pendown()
        for i in range(4):
            huskers.forward(90)
            huskers.right(90)
        huskers.penup()
        huskers.goto(-30,30)
        huskers.pendown()
        for i in range(4):
            huskers.forward(110)
            huskers.right(90)
        huskers.penup()
        huskers.goto(-40,40)
        huskers.pendown()
        for i in range(4):
            huskers.forward(130)
            huskers.right(90)
        huskers.penup()
        huskers.goto(-40,40)
        huskers.pendown()
    if number == 3:
        for i in range(4):
            BOGO.forward(50)
            BOGO.right(90)
        BOGO.penup()
        BOGO.goto(-10,10)
        BOGO.pendown()
        for i in range(4):
            BOGO.forward(70)
            BOGO.right(90)
        BOGO.penup()
        BOGO.goto(-20,20)
        BOGO.pendown()
        for i in range(4):
            BOGO.forward(90)
            BOGO.right(90)
        BOGO.penup()
        BOGO.goto(-30,30)
        BOGO.pendown()
     
        
def main():
    myTurtle = turtle.Turtle()
    
    # drawSquare(myTurtle, 100)
    
    # drawPolygon(myTurtle, 5) #draws a pentagon
    # drawPolygon(myTurtle, 8) #draws an octogon

    # fillCorner(myTurtle, 2) #draws a square with top right corner filled in.
    # fillCorner(myTurtle, 3) #draws a square bottom left corner filled in.

    # squaresInSquares(myTurtle, 5) #draws 5 concentric squares
    # squaresInSquares(myTurtle, 3) #draws 3 concentric squares


main()

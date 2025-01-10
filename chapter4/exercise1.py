"""Write a void (non-fruitful) function to draw a square. Use it in a program to draw the image shown below.
Assume each side is 20 units. (Hint: notice that the turtle has already moved away from the ending point of the last
square when the program ends)"""

import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

def square(t,w,a):
    for i in range(4):
        t.forward(w)
        t.left(a)
    t.penup()
    t.forward(40)
    t.pendown()

for i in range(5):
    square(tess, 20, 90)

wn.mainloop()

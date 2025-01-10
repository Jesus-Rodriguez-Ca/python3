"""Write a program to draw this. Assume the innermost square is 20 units per side, and each
successive square is 20 units bigger, per side, than the one inside it."""

import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

def square(t,w,a):
    for i in range(4):
        t.forward(w)
        t.left(a)
    t.penup()
    t.backward(10)
    t.right(90)
    t.forward(10)
    t.left(90)
    t.pendown()

for i in range(6):
    square(tess, 20 * i, 90)

wn.mainloop()
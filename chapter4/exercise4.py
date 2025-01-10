"Draw this pretty pattern"

import turtle
def pretty():
    wn = turtle.Screen()
    t = turtle.Turtle()
    t.speed(500)
    for i in range(21):
        t.forward(70)
        t.penup()
        t.backward(70)
        t.left(18)
        t.pendown()
    t.home()
    t.backward(70)
    t.right(80)
    
    for i in range(20):
        t.forward(22)
        t.left(18)
   
   
    t.backward(60)
    for i in range(6):
        for i in range(4):
            t.forward(140)
            t.left(90)
        t.penup()
        t.forward(20)
        t.right(65)
        t.forward(20)
        t.left(84)
        t.pendown()
    wn.mainloop()
pretty()
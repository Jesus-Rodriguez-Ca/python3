"""If you were going to draw a regular polygon with 18 sides, what angle would you nedd to turn the turtle at each corner"""


import turtle

def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    sides = 18
    angle = 360 / sides

    for i in range(sides):
        tess.forward(45)
        tess.left(angle)

    wn.mainloop()
main()
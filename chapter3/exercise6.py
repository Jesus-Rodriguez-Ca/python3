"""Use for loop to make a turtle draw these regular polygons(regular means all sides the same lenghts, all angles the same)"""
import turtle
def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    
    
    for i in range(3):
        tess.forward(120)
        tess.left(120)
    
    tess.penup()
    tess.backward(140)
    tess.pendown()

    for i in range(4):
        tess.forward(120)
        tess.left(90)

    tess.penup()
    tess.backward(140)
    tess.pendown()

    for i in range(6):
        tess.forward(80)
        tess.left(60)

    tess.penup()
    tess.forward(450)
    tess.pendown()

    for i in range(8):
        tess.forward(60)
        tess.left(45)

    wn.mainloop()
main()


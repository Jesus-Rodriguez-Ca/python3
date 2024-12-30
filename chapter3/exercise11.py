"""Wrire a program to draw a shape like this: A 5 points star"""

import turtle
def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    
    for i in range(5):
        tess.hideturtle()
        tess.left(-144)
        tess.forward(150)
        
        
    wn.mainloop()
main() 
"""Suppose our turtle tess is at heading 0 - facist east. We execute the statement tess.left(3645). 
What does tess do. and what is her final heading"""

# It would go in circles 100 times and ended up facing 45 degrees
import turtle
def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.left(3645)
    wn.mainloop()
main()
"""Enhance you program above to also tell us what the drunk pirate's heading is after he has finished stumbling around.
(Assume he begins at heading 0)"""

import turtle
def main():
    steps = 100
    angles = [160, -43 , 270 , -97 , -43, 200, -940, 17, -860]

    wn = turtle.Screen()
    pirate = turtle.Turtle()

    for i in angles:
        pirate.forward(steps)
        pirate.right(i)

    wn.mainloop()
    
main()
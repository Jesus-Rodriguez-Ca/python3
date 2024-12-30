"""A drunk pirate makes a random turn and then takes 100 steps forward, makes another random turn, take another 100 steps,
turns another random amount , ect. A social science student records the angle of each turn before the next 100 steps are taken.
Her experimental datsa is [160, -43 , 270 , -97 , -43, 200, -940, 17, -860]. (Positive angles are counter-clockwise). 
Use a turtle to draw the path taken by our drunken friend.
"""
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
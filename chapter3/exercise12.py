"""Write a program to draw a face of a clock that lokks something like this:"""


import turtle
def main():
    wn = turtle.Screen()
    tess = turtle.Turtle()
    tess.speed(5)
    
    for i in range(12):
        tess.penup()
        tess.shape("arrow")
        tess.forward(120)
        tess.pendown()
        tess.forward(10)
        tess.penup()
        tess.forward(20)
        

        tess.shape("turtle")
        tess.stamp()
        tess.backward(150)
        tess.right(30)

        
        
    wn.mainloop()
main() 
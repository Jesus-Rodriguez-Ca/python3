"""Write a void function draw_poly(t, n, sz) which makes a turtle draw a regular polygon.
When called with draw_poly(tess, 8, 50), it will draw a shape like this:"""


import turtle

wn = turtle.Screen()
tess = turtle.Turtle()

def draw_poly(t, n, sz):
    for i in range(n):    
        t.forward(sz)
        t.left(45)
draw_poly(tess, 8, 50)

wn.mainloop()
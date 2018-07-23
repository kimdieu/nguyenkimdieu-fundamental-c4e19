from turtle import *

def draw_star(x, y, length):
    penup()
    goto(x,y)
    pendown()
    for i in range (5):
        forward(length)
        right(144)

draw_star(-94, 160, 150)
mainloop()
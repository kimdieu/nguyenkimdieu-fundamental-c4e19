from turtle import *

def draw_square(length, square_color):
    speed(-1)
    color(square_color)
    for i in range (4):
        forward(length)
        left(90)

draw_square(200, "orange")
mainloop()
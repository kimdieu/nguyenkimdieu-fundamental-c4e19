from turtle import*
shape("turtle")
color("blue")
speed(-1)

edge_length = 120

left(130)

for i in range (100):
    for i in range (4):
        forward(edge_length)
        left(90)
    edge_length -= 2
    right(10)
    if edge_length == 0:
        break

mainloop()
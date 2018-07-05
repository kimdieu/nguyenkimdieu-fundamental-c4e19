from turtle import*
shape("turtle")
colors = ["red", "blue", "brown", "yellow", "grey"]
speed(-1)
# a = 3 

# for y in range (a,8):
#     color(colors[a-3])
#     for i in range (a):
#         forward(100)
#         left(360/a)
#     a += 1
    
# mainloop()
for y in range (5):
    color(colors[y])
    begin_fill()
    for i in range (2):
        forward (80)
        right (90)
        forward (130)
        right(90)
    forward (80)
    end_fill()
mainloop()

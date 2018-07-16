from turtle import*
shape("turtle")
color("red")
speed(-1)

right (30)
for z in range (4):
    for i in range (2):
        for y in range (2):
            forward (100)
            left(60)
        left (60)
    right (90)
mainloop()


# a = 3 
# for y in range (a,7):
#     if a%2!=0:
#         color("red")
#     elif a%2==0:
#         color("blue")
    
#     for i in range (a):
#         forward(100)
#         left(360/a)
#     a += 1
    
# mainloop()

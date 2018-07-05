from turtle import *
shape("turtle")
speed(-1)
color("red")
begin_fill()
for y in range(12):
    for i in range(4):
        forward(100)
        right(90)
    right(30)
end_fill()
mainloop()

                                                # RANDOM
# a = int(input("Enter the number of angle? "))
# b = 360/a
# for i in range (a):
#     forward(100)
#     right(b)
# end_fill()
# mainloop()
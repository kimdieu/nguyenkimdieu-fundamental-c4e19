# from random import randint
# y= randint(0,100)
# if y<40:
#     print (":(")
# elif y<70:
#     print (":)")
# else:
#     print ("rock'n roll")
for i in range (6):
    for y in range (6+1):
        if y >= (6-i):
            print ("*", end=" ")
        else:
            print("-", end=" ")
    print()
    
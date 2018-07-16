from random import randint

y = int(input("Enter a number "))
original_y = y
counting = True
count = 0
while y > 0:
    y = y // 10
    # if y == 0:
    #     counting = False
    count += 1
print("{0} has {1} digit(s)".format(original_y, count))



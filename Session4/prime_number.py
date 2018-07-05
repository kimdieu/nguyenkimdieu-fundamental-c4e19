enter = int(input("Enter a number: "))

# if enter > 3:
#     for i in range (2, enter - 1):
#         # print(i)
#         if enter % i != 0:
#             print("{0} is a prime number".format(enter))
#             break
#         else:
#             print("{0} is not a prime number".format(enter))
#         break
# else:
#     print("{0} is a prime number".format(enter)")
is_prime = True
i = 2
while i <= (enter ** 0.5):
    if enter % i == 0:
        is_prime = False
        break
    i += 1

if is_prime:
    print ("{0} is a prime number".format(enter))

else:
    print ("{0} is not a prime number".format(enter))
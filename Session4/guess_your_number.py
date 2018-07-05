print ("From 0 to 100, think of a number in your head...")
input()

print("""
All you have to do is to answer to my guess
'c' if my guess is 'C'orrect
's if my guess is too 'S'mall
'l' if my guess is too 'L'arge""")
input()

low = 0
high = 100
count = 0

loop = True
while loop:
    mid = (low + high) // 2

    ans = input("Is {0} your number? ".format(mid)).lower()
    # ans = input("").lower()

    if ans == "c":
        print("I knew it!")
        break

    elif ans == "s":
        low = mid

    elif ans =="l":
        high = mid

    count += 1

    if count == 7:
        print("Sorry, your number doesn't exist:( ")
        loop = False
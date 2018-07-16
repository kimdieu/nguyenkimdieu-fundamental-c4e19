from random import randint
y = randint(0,100)
count = 0
while True:
    guess = int(input("Any number? "))
    if y < guess:
        print ("a little too large")
    elif y > guess:
        print ("a little too small")
    elif y == guess:
        print ("BINGOOOO")
        playing = False
        

    count += 1
    if count ==9:
        print("You lose:(")
        break
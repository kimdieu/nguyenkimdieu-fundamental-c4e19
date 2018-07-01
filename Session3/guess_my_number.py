from random import randint
y = randint(0,100)
count = 0
while True:
    guess = int(input("any number"))
    if y < guess:
        print ("a little too large")
    elif y > guess:
        print ("a little too small")
    elif y == guess:
        print ("bingo")
        playing = False
    
    count += 1
    if count ==7:
        print("You lose:(")
        break
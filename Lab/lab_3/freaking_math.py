from random import randint, choice
import evaluate

x = randint(0,10)

y = randint(0,10)

opr = choice(['+','-','*','/'])

res = evaluate.calc(x,y,opr)

# print ("{0} {1} {2} = {3}".format(x,k,y, res))

error = choice([-1,0,1])

dis_res = res + error

print ("* "* 10)
print ("{0} {1} {2} = {3}".format(x,opr,y, dis_res))
print ("* "* 10)

ans = input ("(Y/N)? ".upper())
print ("* "* 10)

if error == 0:
    if ans == "Y":
        print ("YaY")
    elif ans == "N":
        print ("Oopss, wrong")

elif error != 0:
    if ans == "Y":
        print ("Oopss, wrong")
    elif ans == "N":
        print ("YaY")
    
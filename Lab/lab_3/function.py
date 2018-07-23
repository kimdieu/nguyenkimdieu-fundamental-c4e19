x = int(input("x = "))

opr = input("Operation(+,-,*,/): ")

y = int(input("y = "))

if opr == '+':
    tong = x + y 
    print ("* " * 10)
    print ("{0} + {1} = {2}".format(x,y,tong))
    print ("*" * 10)

elif opr == '-':
    tong = x - y 
    print ("* " * 10)
    print ("{0} - {1} = {2}".format(x,y,tong))
    print ("*" * 10)

elif opr == '*':
    tong = x * y 
    print ("* " * 10)
    print ("{0} * {1} = {2}".format(x,y,tong))
    print ("* " * 10)

elif opr == '/':
    tong = x / y 
    print ("* " * 10)
    print ("{0} / {1} = {2}".format(x,y,tong))
    print ("* " * 10)

else:
    print("sorry, your operation is not available:(")
size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Dieu and these are my sheep sizes: ")
print(size)
input()

# max_size = (max(size))
# print("Now my biggest sheep has size {0} let's shear it. ". format(max_size))
# input()

# x = size.index(max_size)
# size[x] = 8

# print ("After shearing, here is my flock: ")
# print (size)
# input()

loop = True
while loop:
    for z in range (3):
        a = 1
        
        for i in range (len(size)):
            print ("MONTH {0}".format(a))
            size[i] += 50
            print ("One month has passed, now here is my flock ")
            print (size)
            input()

            max_size = (max(size))
            print("Now my biggest sheep has size {0} let's shear it. ". format(max_size))
            input()

            x = size.index(max_size)
            size[x] = 8
            print ("After shearing, here is my flock: ")
            print (size)
            input()

            a += 1
            size[i] += 50
            
        break

    # total = sum(size)
    # price = total * 2 

# print("My flock has size in total: {0}".format(total))
# print("I would get {0} *$2 = {1}".format(total,price))
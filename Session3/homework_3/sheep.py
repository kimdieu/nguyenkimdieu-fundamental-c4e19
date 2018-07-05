size = [5, 7, 300, 90, 24, 50, 75]
print("Hello, my name is Dieu and these are my sheep sizes: ")
print(size)
max_size = (max(size))
print("Now my biggest sheep has size {0} let's shear it. ". format(max_size))

x = size.index(max_size)
size[x] = 8

print (size)

# loop = True
# while loop:
for i in range (len(size)):
    size[i] += 50
print(size)

total = sum(size)
price = total * 2 

print("has size in total: {0}".format(total))
print("i get {0} *$2 = {1}".format(total,price))
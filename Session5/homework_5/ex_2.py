numbers = [1,6,8,9,2,1,7,9,6,1,2,9]
print (numbers)

n = int(input("Enter a number: "))

# cach 1 (with 'count')
appearance = numbers.count(n)

print(n, "appears", appearance, "times in my list.")


# cach 2 (without 'count')
freq = sum(freq == n for freq in numbers)

print ("{0} appears {1} times in my list.".format(n,freq))



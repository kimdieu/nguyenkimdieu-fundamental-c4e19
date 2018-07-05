from random import choice

menu = ["people", "tokyo", "gateway"]

item = menu[1]
# print(item)
new_list = []
# word = "champion"
n = list(item)
# print(n)
loop = True
while loop:
    m = choice(n)
    # print (m, end= " ")
    new_list.append(m)
    n.remove(m)
    if len(n) == 0:
        loop = False

print(new_list)

# print()
ans = input("Your answer: ")
loop = True
while loop:
    if ans == item:
        print("BINGO")
        loop = False
    else:
        print("Try again:(")
        

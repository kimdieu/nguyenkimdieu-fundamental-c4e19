clothes = ["T-Shirt", "Sweater"]

loop = True

while loop:
    item = input("Welcome to our shop, what do you want (C, R, U, D)? Press X to Exit ")
    # print("Press X to exit")

    if item == "R" or item == "r":
        print ("Our item:", end = " ")
        print (*clothes, sep=', ')

    elif item == "C" or item == "c":
        y = input("Enter new item: ")
        clothes.append(y)
        print ("Our item: ", end="")
        print(*clothes, sep=", ")

    elif item == "U" or item == "u":
        r = int(input("Update position? "))
        update_clothes = input("New item? ")
        clothes[r-1] = update_clothes
        print ("Our item: ", end="")
        print(*clothes, sep=", ")
        
    elif item == "D" or item == "d":
        loop2 = True
        while loop2:
            m = int(input("Delete position? "))
            if 1 <= m <= len(clothes):
                clothes.pop(m-1)
                print ("Our item: ", end="")
                print (*clothes, sep=', ')
                loop2 = False
            else:
                print("Chosen position not available. Please try again? ")
    
    elif item == "X" or item == 'x':
        loop = False
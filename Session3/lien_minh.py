
menu = ["Kem", "xoi", "Pho", "thit", "tao pho"]

# print(*menu, sep=",")
# print(len(menu))
# menu.append("Che")

# print(*menu, sep=", ")
# print(len(menu))


# print("Hi there, here your favorite channel so far?")
# menu = ["deathnote", "netflix", "fox", "worldcup"]
# print (*menu, sep=", ")
# y = input("wanna add? ")
# menu.append(y)
# print(*menu, sep=", ")

# item = menu[-7]
# print(item)

# for i in range(len(menu)):
#     print(menu[i])


# for index, item in enumerate(menu):
#     print(index, item)

# for item in menu:
#     print(item)


# menu[1] = "Che"
# print(*menu, sep=", ")

# fav = ["death note", "coding", "painting"]
# for index, item in enumerate(fav):
#     print(index +1, item)
# print("*" * 20)
# r = int(input("position you want to update? "))
# update_fav = input("your replacement? ")
# fav[r-1] = update_fav
# for index, item in enumerate(fav):
#     print(index +1, item)


            # cach xoa 
            #     1. remove
            #     2. del
            #     3. pop
            
# menu. remove ('xoi')
# print(menu)

# del menu[2]
# print(menu)

menu.pop(1)
print(*menu, sep=", ")
    
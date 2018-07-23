def get_even_list(l):
    new_list = []
    for num in l:
        if num%2 ==0:
            new_list.append(num)
    return (new_list)

# # ex_9
# even_list = get_even_list([1,4,5,-1,10])
# print (even_list)


# # ex_10
even_list = get_even_list([1, 2, 5, -10, 9, 6])

if set(even_list) == set([2, -10, 6]):
    print("Your function is correct")
else:
    print("Ooops, bugs detected")



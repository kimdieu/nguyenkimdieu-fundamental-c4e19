def remove_dollar_sign(s):
    
    updated_s = s.replace("$", "")

    return (updated_s)

# # ex_7
# new_s = remove_dollar_sign('$76179$hjsdj$')
# print (new_s)

# # ex_8
string_with_no_dollars = remove_dollar_sign("$80% percent of $life is to show $up")
if string_with_no_dollars == "80% percent of life is to show up":
    print("Your function is correct")
else:
    print("Oops, there's a bug")
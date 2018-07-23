# định nghĩa
# arguments
def calc(x,y,opr):

    res = 0

    if opr == '+':
        return x + y
    elif opr == '-':
        res = x - y
    elif opr == '*':
        res = x * y
    elif opr == '/':
        res = x / y

    return res

# gọi 
# result = calc(4, 5,'*')
# print(result)


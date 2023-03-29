# def arithmetic_mean(*args):
#     sum=0
#     b =0
#     for i in args:
#         a=int(i)
#         sum+=a
#         b +=1 

#     return sum/b
# print(arithmetic_mean(2,4,7,8))


def largest_number(*args):
    """
    Function return largest number of input number
    """
    larg= 0
    for i in args:
        if i>larg:
            larg=i
    return larg

print (largest_number(1,4,9,23,5))
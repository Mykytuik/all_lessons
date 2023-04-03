import square 
print("Enter figur:")
str=input()
if str=="rectangle":
    print("Enter a and b:")
    # a=int(input())
    # print("Enter b:")
    # b=int(input())
    print(square.square_rectangle(int(input()),int(input())))
elif str=="triangle":
    print("Enter h and a:")
    print(square.square_triangle(int(input()),int(input())))
elif str=="circle":
    print("Enter r:")
    print(square.square_circle(int(input())))

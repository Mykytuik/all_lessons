#  print("Write lenght of list")
# a=int(input())
# L=[]

# for i in range(a):
#     print("Write number")
#     L.append(int(input()))
# min=L[0]
# max=L[0]
# for m in L:
#     if m<min:
#         min=m
#     elif m>max:
#         max=m
# print(f"Min:{min}, Max:{max}")
 

# home
# Even=[]; Odd=[]; Else=[]
# for i in range(1,11):
#     if i %2==0:
#         Even.append(i)
#     if i%3==0:
#         Odd.append(i)
#     if i%2!=0 and i%3!=0:
#         Else.append(i)
# print(f"Even:{Even}, Odd:{Odd}, Not divisible by 2 and 3:{Else} ")

# home2
message=False
while message==False:
    print("Enter login:")
    String_Mes=str(input())
    if String_Mes=="First":
        message=True
        print("Login is correct!")
    elif String_Mes!="First":
        print("Try again:")

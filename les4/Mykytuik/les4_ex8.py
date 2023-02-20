#Factorial
value=1
inp=int(input("Factorial from:"))
if -1<inp<=1:
    print("Factorial:1")
elif inp<0:
    print("Factorial non positive number don`t exist")
else:
    for var in range(1,inp+1):
        value*=var
    print(f"Factorial:{value}") 
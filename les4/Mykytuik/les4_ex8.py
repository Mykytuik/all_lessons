#Factorial
value=1
inp=int(input("Factorial from:"))
for var in range(inp+1):
    if inp<=1:
        print("Factorial:1")
    elif var<=1:
        pass
    else:
        value*=var
print(f"Factorial:{value}") 
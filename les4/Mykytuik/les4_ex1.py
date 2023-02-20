print ("Write a:")
a=int(input())
print ("Write b:")
b=int(input())
if a == b:
    print(f"a({a})=b({b})")
elif a<b:
    print(f"a({a})<b({b})")
else :
    print(f"a({a})>b({b})") 

print ("Write a:")
a=int(input())
if a % 2 == 0 :
    print (f"a({a})- парне")
else:
    print (f"a({a})- непарне")
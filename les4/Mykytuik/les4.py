""" print ("Write a:")
a=int(input())
print ("Write b:")
b=int(input())
if a == b:
    print(f"a({a})=b({b})")
elif a<b:
    print(f"a({a})<b({b})")
else :
    print(f"a({a})>b({b})") """

""" print ("Write a:")
a=int(input())
if a % 2 == 0 :
    print (f"a({a})- парне")
else:
    print (f"a({a})- непарне") """
 

# for val in range(2,100,2):
#    print(val)
# value=1
# while value < 100:
#    if value%2==0:
#        print(value)
#    value+=1    

#    if val%2==0:
#        continue
#    else:
#        print(val)
# for val in list(range(int(input("Write A:")))):
#    if val%2!=0:
#        print(val)
#        break
#Fibonachi
fibo=0
value=1
val=0
c=int(input("Write A:"))
while fibo <= c:
   if fibo>c:
       break
   print(fibo)
   fibo=val+value
   val=value
   value=fibo
list =[0,1,2,3,4,5,6]
print(type(list[0]))
for var in list:
   list[var]= float(var)
   
print(type(list[1]))

#Factorial
value=1
inp=int(input())
for var in range(inp+1):
    if inp<=1:
        print("Factorial:1")
    elif var<=1:
        pass
    else:
        value*=var
print(f"Factorial:{value}")        
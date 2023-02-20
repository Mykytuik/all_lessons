#Fibonachi
fibo=0
value=1
val=0
A=int(input("Write A:"))
while fibo <= A:
   if fibo>A:
       break
   print(fibo)
   fibo=val+value
   val=value
   value=fibo
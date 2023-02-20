# V-1
print(list(range(2,100,2)))
#V-2
for val in range(2,100,2):
   print(val)
#Ex-3
val=0
while val<100:
   
   if val%2==0:
       continue
   else:
       print(val)
val+=1
   
   


for val in list(range(int(input("Write A:")))):
   if val%2!=0:
       print(val)
       break
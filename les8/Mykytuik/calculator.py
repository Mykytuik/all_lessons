suma=0
def addition(*args):
    
    for i in args:
        global suma
        if suma==0:
            suma=args[0]
        else:
            suma+=i
    print(suma)

def subtraction(*args):
    global suma
    suma=0
    for i in args:
        
        
        if suma==0:
            suma=args[0]
        else:
            suma-=i
    print(suma)
def multiplication(*args):
    suma=1
    for i in args:
        suma*=i
    print(suma)
divis=0
def division (*args:int):
   for i in args:
       global divis
       if divis==0:
           divis=i
       else:
           divis/=i
   print(divis)
    

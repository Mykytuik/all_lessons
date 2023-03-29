
def square(figur ,*args:float):
    S= float
    
    if figur =="rectangle" and len(args)==2:
        for i in args:
            S*=i
    elif figur =="triangle" and len(args)==2:
        S=0.5*args[0]*args[1]
    elif figur =="circle" and len(args)==1:
        S= 3.14*(args[0]**2)
    else:
        print("Eror, check the spelling of the shape nape or the number of entered parameters")
    return S
print(square("circle", 3))
    #print( square(input(),input(),input()))
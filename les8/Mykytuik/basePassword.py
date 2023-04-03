import string
dic_Password={}
def printed_L():
    print("Login or Sign up:")
    str=input()
    str_Login="Login"
    str_Sign_up="Sign up"
    if str==str_Login :
        print("Enter login:")
        Log=input()
        print("Enter password:")
        Pas=input()
        Login(Log,Pas)
    elif str==str_Sign_up:
        print("Enter login:")
        Log=input()
        print("Enter password:")
        Pas=input()
        Logup(Log,Pas)
    else:
        print("Choose login or sign up!")
        printed_L()
lower=0
upper=0
digit=0
n=0
def Logup(Login,password:str):
    """
    The function registers a new user
    """
    global dic_Password
    global lower,upper,digit,n
    
    if len(password)<6 or len(password)>16:
        print("Minimum length 6 characters and maximum length 16 characters")
        
    
    for m in password:
        
        if m.islower() !=False:
            lower+=1
        if m.isupper()!=False:
            upper+=1
        if m.isdigit()!=False:
            digit+=1
        if "@"in m or "$"in m or "#"in m:
            n+=1
        
        #return i
    if lower==0 or upper==0 or digit==0 or n==0:
        print("At least 1 letter between [a-z] and 1 letter between [A-Z]. \n At least 1 number between [0-9].\n At least 1 character fro [$#@].")
        print("Try again:")
        password=str(input())
        Logup(Login,password)  
    if lower>0 and upper>0 and digit>0 and n>0:
        print("Registration is succesful!")



def Login(Login,password):
    if Login in dic_Password:
        if dic_Password.get(Login)==password:
            print("Good!")
        elif dic_Password.get(Login)!=password:
            print("Wrong password")
    elif Login not in dic_Password:
        print("Wrong login")    
from random import randint
a=randint(0,100)
def game_number(number:int):
    global a
    print (a)
    while a!=number:
        
        if a==number:
            print("Congratulations! You won!")
        elif number>a:
            print("Try again. The number is less")
        elif number<a:
            print("Try again. The number is higher")
        print("Enter number:")
        number=int(input())
        if a==number:
            print("Congratulations! You won!")
game_number(int(input()))
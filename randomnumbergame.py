import random
n=random.randint(0,99)
a=1
nn=int(input("Please enter a number44 between 0 and 99(including)"))
while nn!=n:
   
    if nn>99 or nn< 0:
        print("you entered number out of range!")
        print("do you want to enter another number")
        print("press Y to enter another number and other characters to exit!")
        an=str(input())
        if an=='y' or 'Y':
            nn==int(input("Please enter a number between 1 and 9(including)"))
    else:
        if nn>n:
            print("you guessed higher than the number")
        else:
            print("you guessed less than the number")
    ab=str(input("want to enter another guess,press quit to quit, anything other to continue"))
    if ab=='quit':
        break
    else:
        nn=int(input("Please enter a number between 0 and 99(including)"))
        a=a+1
if nn==n: 
    print("the number you last enterred",nn)
    print("the random number is",n)
    print("Bingo!, you did correctly guessed the random number")
    print("thank you for playing the game")
    print("the total attempts you made is: ",a)

else:
    print("the total attempts you made is: ",a)
    print("thank you for playing this game!")

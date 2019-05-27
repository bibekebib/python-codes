import random
n=1
c=str(input("enter any word=")).upper()
with open ("file.txt","r") as a:
    lines=list(a)
b=random.choice(lines)
print(b)

if b==c:

    print("you made correct choice") 
while c!=b:
    #print(lines)

    z=str(input("you are wrong! Do you want to contunue? If yes, press 'Y' else press any other character=="))
    if z=='Y' or 'y':
                c=str(input("enter any word=")).upper()
                n=n+1
    if c==b:
                    print("you made correct choice")
                    break
    else:
                print("sorry, you couldn't guessed the word correctly!")
                break

print("The random word generated is",b, "The last word you guessed",c)
print("the number of attempts you made",n)
#input part
name=str(input("enter you name"))
age=int(input("enter you age"))
n=int(input("enter any number you like"))

import datetime
now = datetime.datetime.now()
hundred = now.year+100-age
while n!=0:
    print("your name is"+ name)
    print("your age is" ,age)
    print("you will be hundred years in", hundred)
    n=n-1
print("finished")

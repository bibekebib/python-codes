import random
b=''
n=int(input("how many charcter long password do you want to generate? "))
for i in range (n):
    a=random.choice('ABCDvwxyz01EFGHIJUVWXYZ@#$%@bcdefghijklmnopqrstu2KLMNOPQRST3456789!&')
    b=b+a
    i=i+1
print(b)
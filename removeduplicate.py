from functools import reduce
a=[]
a=list(map(str, input().split()))
b=[]
for x in a:
    if x not in b:
        b.append(x)
print(b)
from array import *
i=array('i',[])
n=int(input("enter the length"))
for e in range(n):
    x=int(input("enter val"))
    i.append(x)
print(i)
print(i[::-1])


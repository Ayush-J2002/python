

from array import *
x=array('i',[])
n=int(input("enter length"))
for i in range(n):
        v=int(input("enter values"))
        x.append(v)
print(x)

for e in range(n):
        if(e==2):
                continue
        print(x[e])






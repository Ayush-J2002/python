from array import *
ar=array('i',[])
t=0
x=int(input("enter length"))
for i in range(x):

    y=int(input("enter vals :"))
    ar.append(y)

print("without sort",ar)
for i in range(x):
    for j in range(i+1,x):
        if(ar[i]>ar[j]):
            t=ar[i]
            ar[i]=ar[j]
            ar[j]=t


print("with sort",ar)
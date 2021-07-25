from array import *
arr=array('i',[])
x=int(input("enter length"))
for i in range(x):
    n=int(input('enter val'))
    arr.append(n)

max=0
for e in range(len(arr)):
    if(max<arr[i]):
        max=arr[i]


print(max)

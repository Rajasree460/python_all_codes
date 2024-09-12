#array insert
from array import *
def array_insert(arr):
    a=int(input("enter the pos to which the element is to be inserted:"))
    b=int(input("enter the element to be inserted:"))
    arr.insert(a,b)
    print("after insertion the array:",arr)
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
print("the original array:",arr)  
array_insert(arr)  
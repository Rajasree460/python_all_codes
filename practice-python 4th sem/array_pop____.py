#array pop
from array import *
def array_insert(arr):
    a=int(input("enter the pos from which the element is to be deleted:"))
    arr.pop(a)
    print("after deletion the array:",arr)
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
print("the original array:",arr)  
array_insert(arr)  
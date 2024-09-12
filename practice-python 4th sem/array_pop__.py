#array pop
from array import *
def array_pop(arr):
    arr.pop(2)
#main func
arr=[]
n=int(input("enter the array size:")) 
print("enter ur array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
print("original array:",arr)
array_pop(arr)
print("after deletion the arra is:",arr)       
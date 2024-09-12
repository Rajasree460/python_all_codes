#swapp pos in array
from array import *
def swapp_pos(arr,pos1,pos2):
    arr[pos1],arr[pos2]=arr[pos2],arr[pos1]
    print("after swapping the array is:",arr)
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
pos1=int(input("enter the 1st pos:"))  
pos2=int(input("enter the 2nd pos:"))      
print("the original array:",arr)
swapp_pos(arr,pos1,pos2)
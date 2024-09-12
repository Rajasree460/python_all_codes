#array insert
from array import*
def array_insert(list):
    list.insert(2,9)
    print("after pop the  array:",list) 
#main func
list=[]
n=int(input("the size of array:"))
print("take ur array elements")
for i in range(0,n):
    l=int(input())
    list.append(l)
print("original array:",list)  
array_insert(list)  
# print("after pop the  array:",list)    
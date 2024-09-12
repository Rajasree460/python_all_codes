#array pop
#1
# from array import*
# array=[1,2,3,4,5]
# print("original array:",array)
# array.pop(2)
# print("after pop the  array:",array)

#2
# from array import*
# list=[]
# n=int(input("the size of array:"))
# print("take ur array elements")
# for i in range(0,n):
#     l=int(input())
#     list.append(l)
# print("original array:",list)
# list.pop(2)
# print("after pop the  array:",list)  
 
#
from array import*
def array_pop(list):
    list.pop(2) 
#main func
list=[]
n=int(input("the size of array:"))
print("take ur array elements")
for i in range(0,n):
    l=int(input())
    list.append(l)
print("original array:",list)  
array_pop(list)  
print("after pop the  array:",list)
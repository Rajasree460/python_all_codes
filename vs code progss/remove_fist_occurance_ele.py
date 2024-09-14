# remove the first occurrence of a specific element of an array
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 1, 9, 3])
print("Original array:")
for i in array_num:
   print(i)
array_num.remove(3) #here,we can see if we count from the oth index of the array 3 comes fir 1 time for count=2,for count=4 3 comes for 2 times so we have to dlt the 3 for count =2
print("after deletion the new array: ")
for i in array_num:
   print(i)

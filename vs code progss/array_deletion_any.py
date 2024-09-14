#array deletion from any position
from array import *
array_num = array('i', [1,2,3,4,5])
print("Original array:")
for i in array_num:
   print(i)
array_num.pop(2)  #deleting the 3rd item form the array
print("after deleting from any location the new array: ")
for i in array_num:
   print(i)

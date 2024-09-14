#insert any position in array by location/index
from array import *
array_num = array('i', [1,2,3,4,5])
print("Original array:")
for i in array_num:
   print(i)
array_num.insert(2,9)    #Insert new value 4 before 3
print("after inserting the new array: ")
for i in array_num:
   print(i)
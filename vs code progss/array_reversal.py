#array reversal
from array import *
array_num = array('i', [1,2,3,4,5])
print("Original array:")
for i in array_num:
   print(i)
array_num.reverse()
print("Reverse the order of the items:")
for i in array_num:
   print(i)

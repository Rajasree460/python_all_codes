#multiple occurance of same element in an array
from array import *
array_num = array('i', [1, 3, 5, 3, 7, 9, 3])
print("Original array:")
for i in array_num:
   print(i)
print("Number of occurrences of the number in the said array: "+str(array_num.count(3)))

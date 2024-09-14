#convert an array to a normal list with the same array elements
from array import *
array_num = array('i', [1,2,3,4,5])
print("Original array: ")
for i in array_num:
   print(i)
num_list = array_num.tolist() # convert an array to an ordinary list with the same items
print("after conversion of array into a normal list the list is:")
print(num_list)
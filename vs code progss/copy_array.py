#array copy
from array import *
array_num = [1, 2, 6, -8]
array_copy = array('i', [])
print("Original array: " + str(array_num))  #for horizontal representation of array
# print("Original array:")                  #for vertical representation of array
# for i in array_num:
#    print(i)                               #it will work like new line(\n) at each iteration
array_copy.fromlist(array_num)  #Append items from the list
print("copied array: "+str(array_num))
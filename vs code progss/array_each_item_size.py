#the size of each item of an array
from array import *
array_num = array('i', [1,2,3,4,5])
for i in array_num:
   print(i)
print("Length in bytes of one array item: "+str(array_num.itemsize))
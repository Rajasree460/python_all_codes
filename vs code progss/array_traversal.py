#Write a Python program to create an array of 5 integers and display the array items. Access individual elements through indexes.
from array import *
array_num = array('i', [1,3,5,7,9])
for i in array_num:  #for print the whole array(exchange of for(int i=0;i<n(lengthof array);i++) 
 print(i)
print("Access first three items individually")
print(array_num[0])
print(array_num[1])
print(array_num[2])
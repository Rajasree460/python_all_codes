#find the memory size of some lists(by __sizeof__(),inbuild function)
# Define an empty list in the program  
emptyList = []  #value=40
# Printing size of empty list  
print("Internal memory size of an empty list: ", emptyList.__sizeof__())  
# Define some lists with elements  
a = [24]  #val=40+8*1
b = [24, 26, 31, 6]  #val=40+8*4
c = [1, 2, 6, 5, 415, 9, 23, 29]  
d = [4, 5, 12, 3, 2, 9, 20, 40, 32, 64]  
# Printing internal memory size of lists  
print("Memory size of first list: ", a.__sizeof__())  
print("Memory size of second list: ", b.__sizeof__())  
print("Memory size of third list: ", c.__sizeof__())  
print("Memory size of fourth list: ", d.__sizeof__())
#print the sum of all elements in an array
arr = [1, 2, 3, 4, 5]; 
sum = 0; 
 
#Loop through the array to calculate sum of elements 
for i in range(0, len(arr)): 
 sum = sum + arr[i]; 
#as we have not import the array so we cant' use any func of array
 
print("Sum of all the elements of an array: " + str(sum)); 
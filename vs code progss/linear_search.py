#Linear Search
def linear_Search(list1, n, key): 
 
 # Searching list1 sequentially 
 for i in range(0, n): 
  if (list1[i] == key): 
   return i 
 return -1 
 
#main func 
list1 = [1 ,3, 5, 4, 7, 9] 
key = 7 #the elemeant to be searched
 
n = len(list1) 
res = linear_Search(list1, n, key) 
if(res == -1): 
 print("Element not found") 
else: 
 print("Element found at index: ", res) 
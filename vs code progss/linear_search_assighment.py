#Linear Search
def linear_Search(arr, n, key): 
  
 for i in range(0, n): 
  if (arr[i] == key): 
   return i 
 return -1 
 
#main func 
arr = []  
n=int(input("enter the length of your array:"))
print("take your array element:")
for i in range(0,n):  
    l=int(input())
    arr.append(l)
print("The array given is: ", arr) 
n = len(arr)
key=int(input("enter the value to be searched:"))
print("the element that has to be searched:",key)
index = linear_Search(arr, n, key) 
if index != -1:
    print("Element is present at index " + str(index))
else:
    print("Element Not found")
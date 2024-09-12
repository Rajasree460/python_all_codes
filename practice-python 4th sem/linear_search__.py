#linear search
def linear_search(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i
    return -1    
#main func
arr=[]
n=int(input("enter the array size:")) 
print("enter ur array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
print("original array:",arr)
a=int(input("enter the element to be searched:"))
print("the element to be searched:",a)
id=linear_search(arr,a)
if id==-1:
    print("element not found")
else:
    print("element found at index or location:",id)                
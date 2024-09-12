#linear sesrcg
def linear_search(arr,key):
    for i in range(0,len(arr)):
        if arr[i]==key:
            return i
    return -1
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
a=int(input("enter the element to be searched:"))
print("the element to be searched:",a)
print("the original array:",arr)
id=linear_search(arr,a)
if id==-1:
    print("element no found")
else:
    print("element found at the loc:",id)    
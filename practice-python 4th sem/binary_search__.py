#binary search
def binary_search(arr,low,high,key):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==key:
            return mid
        elif arr[mid]<key:
            return binary_search(arr,mid+1,high,key)
        elif arr[mid]>key:
            return binary_search(arr,low,mid-1,key)
    else:
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
id=binary_search(arr,0,n,a)
if id==-1:
    print("element not found")
else:
    print("element found at index or location:",id)                
#binary search
def binary_search(arr,low,high,key):
    if high>=low:
        min=(high+low)//2
        if arr[min]==key:
            return min
        elif arr[min]<key:
            return binary_search(arr,min+1,high,key)
        elif arr[min]>key:
            return binary_search(arr,low,min-1,key)
    else:
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
id=binary_search(arr,0,n,a)
if id==-1:
    print("element no found")
else:
    print("element found at the loc:",id)           
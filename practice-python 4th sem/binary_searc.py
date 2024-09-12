#binary search
def binary_search(arr,low,high,a):
    if high>=low:
        mid=(low+high)//2
        if arr[mid]==a:
            return mid
        elif arr[mid]<a:
            return  binary_search(arr,mid+1,high,a)
        else:
            return  binary_search(arr,low,mid-1,a)
    else:
        return -1        
#main func
arr=[]
n=int(input("enter the length of your array:"))
print("take your array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
print("your array:",arr)
# for i in range(0,n):
#     if arr[i+1]<arr[i]:
#         (arr[i],arr[i+1])=(arr[i+1],arr[i])
#print("after sorting the array is:",arr)
a = int(input("enter the value to be searched:"))
print("The element to be found is: ", a)
id=binary_search(arr,0,len(arr)-1,a)   
if id==-1:
    print("element not found")   
else:
    print("element foundat indes:"+str(id))      
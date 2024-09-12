#linear search
def linear_search(arr,n,key):
    for i in range(0,n):
        if arr[i]==key:
            return i
    return -1
#main func
arr=[]
n1=int(input("enter the length of your array:"))
print("take your array elements:")
for i in range(0,n1):
    l=int(input())
    arr.append(l)
print("your array:",arr)
a=int(input("enter your element to be searched:")) 
print("the searched element:",a)   
id=linear_search(arr,len(arr),a)
if(id==-1):
    print("the element not found")
else:
    print("the element found at index:",id)
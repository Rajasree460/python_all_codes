#binary search
def bubble_sort(arr,low,high,key):
    if high>=low:
      mid=(low+high)//2
      if arr[mid]==key:
          return mid
      elif arr[mid]<a:
          return bubble_sort(arr,mid+1,high,key)
      elif arr[mid]>a:
          return bubble_sort(arr,low,mid-1,key)
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
a=int(input("enter your element to be searched:")) 
print("the searched element:",a)   
id=bubble_sort(arr,0,len(arr),a)
if(id==-1):
    print("the element not found")
else:
    print("the element found at index:",id)    
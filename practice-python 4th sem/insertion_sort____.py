#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp
    print("after sorting the array is:",arr)
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
print("the original array:",arr) 
insertion_sort(arr)
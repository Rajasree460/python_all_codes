#bubble sort
def bubble_sort_a(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]>arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("after sorting(ascending) the array is:",arr)   
def bubble_sort_d(arr):
    for i in range(0,len(arr)):
        for j in range(i+1,len(arr)):
            if arr[i]<arr[j]:
                temp=arr[i]
                arr[i]=arr[j]
                arr[j]=temp
    print("after sorting(descending) the array is:",arr)  
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
print("the original array:",arr) 
bubble_sort_a(arr) 
bubble_sort_d(arr)              
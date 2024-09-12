#insertion sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        j=i-1
        temp=arr[i]
        while j>=0 and arr[j]>temp:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp
    print("after sorting the array:",arr)            
#main func
arr=[]
n=int(input("enter the array size:")) 
print("enter ur array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
print("original array:",arr) 
insertion_sort(arr)
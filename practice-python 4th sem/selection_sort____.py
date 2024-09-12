#selection sort
def selection_sort(arr):
    for i in range(0,len(arr)):
        min_id=i
        for j in range(i+1,len(arr)):
            if arr[j]<arr[i]:
                min_id=j
                arr[i],arr[min_id]=arr[min_id],arr[i]
    print("after sorting the array is:",arr)            
#main func
arr=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    arr.append(l)
print("the original array:",arr) 
selection_sort(arr)
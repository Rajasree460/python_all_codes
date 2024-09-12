#selection sort
def selection_sort(arr):
    for i in range(len(arr)):
        min_id=i
        for j in range(i+1,len(arr)):
            if arr[min_id]<arr[j]:
                min_id=j
            (arr[i],arr[min_id])=(arr[min_id],arr[i])    
#main func
arr=[]
n=int(input("enter the length of your array:"))
print("take your array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
print("your array:",arr)
# for i in arr:
#     print(i,end=" ")    
#print()       
print("after sorting the array in ascending order:",arr)
         
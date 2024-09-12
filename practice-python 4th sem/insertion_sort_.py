#insertion_sort
def insertion_sort(arr):
    for i in range(1,len(arr)):
        temp=arr[i]
        j=i-1
        while j>=0 and temp<arr[j]:
            arr[j+1]=arr[j]
            j=j-1
            arr[j+1]=temp
#main func 
arr = [] #user input
n=int(input("enter the length of your array:"))
print("take your array element:")
for i in range(0,n): 
 l=int(input())
 arr.append(l)
print("The array given is: ", arr)
insertion_sort(arr)
print("Array after sorting:",arr)            
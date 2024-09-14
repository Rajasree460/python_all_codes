#binary search user defined
def binary_search(arr, a, low, high):
    
    if high >= low:

        mid = low + (high - low)//2

        # If found at mid, then return it
        if arr[mid] == a:
            return mid

        # Search the left half
        elif arr[mid] > a:
            return binary_search(arr, a, low, mid-1)

        # Search the right half
        else:
            return binary_search(arr, a, mid + 1, high)

    else:
        return -1

#main func
arr = []  #user input
n=int(input("enter the length of your array:"))
print("take your array element:")
for i in range(0,n):  #sorted array no need to do any kind of sort
    l=int(input())
    arr.append(l)
print("The array given is: ", arr)
a = int(input("enter the value to be searched:"))
print("The element to be found is: ", a)

index = binary_search(arr, a, 0, len(arr)-1)

if index != -1:
    print("Element is present at index " + str(index))
else:
    print("Not found")
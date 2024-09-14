#selection sort using python by finding min_index
def selectionsort(array,size):
    for i in range(size):
        min_index=i
        for j in range(i+1,size):
            #select the min element in every iteration
            if array[j]<array[min_index]:
                min_index=j
            #swapping the elements to sort the array
            (array[i],array[min_index])=(array[min_index],array[i])  
#main func
arr=[8,6,2,5,7]
size=len(arr)
print("the unsorted array is:",arr) 
selectionsort(arr,size)       
print("the array after sorting in ascending order by selection sort is:") 
print(arr) 
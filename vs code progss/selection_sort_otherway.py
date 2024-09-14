#selection sort another way
def selection_sort(array,size):
    min=array[0]
    i=0
    for j in range(i+1,size):
        for i in range(0,size):
            if array[i]<=min:
                min=array[i]
        for i in range(0,size):
            array[j],array[i]=array[i],array[j]     
#main func
array=[5,3,4,1,2]
size=len(array)
print("the original array is:",array)
selection_sort(array,size)
print("the array after sorting in ascending order is:",array)              
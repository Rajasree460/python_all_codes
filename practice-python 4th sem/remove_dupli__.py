#remove all duplicate elements from an array
def remove(arr):
    final_list=[]
    for i in arr:
        if i not in final_list:
            final_list.append(i)
    print("after removing the duplicate elements the array is:",final_list)   
#main func
arr=[]
n=int(input("enter the array size:")) 
print("enter ur array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
print("original array:",arr)
remove(arr)        
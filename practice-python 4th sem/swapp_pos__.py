#swapp pos
def swap_pos(arr,pos1,pos2):
    arr[pos1],arr[pos2]=arr[pos2],arr[pos1]
#main func
arr=[]
n=int(input("enter the array size:")) 
print("enter ur array elements:")
for i in range(0,n):
    l=int(input())
    arr.append(l)
pos1=int(input("enter 1st pos to swapp:"))         
pos2=int(input("enter 2nd pos to swapp:"))         
print("original array:",arr)
swap_pos(arr,pos1,pos2)
print("after swapping the array is:",arr)      
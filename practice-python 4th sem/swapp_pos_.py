#swapp position in an array
def swap_pos(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1] 
#main func
list=[]
n=int(input("the size of array:"))
print("take ur array elements")
for i in range(0,n):
    l=int(input())
    list.append(l)
print("original array:",list)  
pos1,pos2=2,4
swap_pos(list,pos1,pos2)
print("after swapping the array:",list)  
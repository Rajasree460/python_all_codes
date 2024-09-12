#swapp positions in an array
def swap(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    print("after swapping:",list)
#main function
list=[1,2,3,4,5]
pos1,pos2=2,4
print("original array:",list)
swap(list,pos1-1,pos2-1)    
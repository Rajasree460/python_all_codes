#swap position of elements in an array
def swappositions(list,pos1,pos2):
    list[pos1],list[pos2]=list[pos2],list[pos1]
    return list
list=[1,9,4,56]
pos1,pos2=1,3
print(swappositions(list,pos1-1,pos2-1))
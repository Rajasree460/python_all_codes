#remove all dupli from a list
def remove(list):
    final_list=[]
    for i in list:
        if i not in final_list:
            final_list.append(i)
    print("after deletion the list is:",final_list)       
#main func
list=[]
n=int(input("enter the size of array:"))
print("enter ur array elements:")
for i in range(0,n):
    l=int(input()) 
    list.append(l)
print("the original array:",list)
remove(list)
#remove all duplicate elements from an list
def remove(list):
    final_list=[]
    for i in list:
        if i not in final_list:
            final_list.append(i)
    return final_list
#main func
list=[]
n=int(input("enter the length of your list:"))
print("take your list elements:")
for i in range(0,n):
    l=int(input())
    list.append(l)
print("your array:",list)   
print("after removing the list:",remove(list))     
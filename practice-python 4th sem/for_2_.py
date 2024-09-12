#for ex 2
def func(l,u):
    for i in range(l,u+1):
     print(i,i**2)
#main func
llimit=int(input("enter the lower lim:")) 
ulimit=int(input("enter the upper lim:"))   
func(llimit,ulimit)
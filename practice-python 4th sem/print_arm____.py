#print armstrong in range
def print_arm(l,u):
    for i in range(l,u+1):
        sum=0
        copy=i
        while i!=0:
            rem=i%10
            sum=sum+(rem*rem*rem)
            i=i//10
        if(copy==sum):
            print("arm:",copy)
#main func
llim=int(input("enter the lower lim:")) 
ulim=int(input("enter the upper lim:"))     
print_arm(llim,ulim)           
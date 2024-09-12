#armstrong in range
def armstrong_range(l,u):
    for i in range(l,u+1):
        sum=0
        k=i
        while i!=0:
            rem=i%10
            sum=sum+(rem*rem*rem)
            i=i//10
        if k==sum:
          print("arm:",k)
#main func
llim=int(input("enter lower lim no:"))                   
ulim=int(input("enter upper lim no:"))
armstrong_range(llim,ulim)
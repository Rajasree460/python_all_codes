#odd even range
def odd_even_range(l,u):
    for i in range(l,u+1):
        n=i
        if n%2==0:
             print("even:",n)
        else:
            print("odd:",n)
#main func
llim=int(input("enter lower lim:"))
ulim=int(input("enter upper lim:"))
odd_even_range(llim,ulim)                      
#print armstrong in range
def print_arm(l,u):
     for i in range(l,u+1):
         sum=0
         copy=i
         while i!=0:
             rem=i%10
             sum=sum+(rem*rem*rem)
             i=i//10
         if copy==sum:
             print("armstrong:",copy)
#main func
l=int(input("enter llim:"))  
u=int(input("enter ulim:"))     
print_arm(l,u)                 
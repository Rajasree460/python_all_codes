#print armstrong no. in range 1 to 1000
def range_Armstrong(llimit,ulimit):
    for num in range(llimit,ulimit+1):
        copy=num
        sum=0
        while(copy!=0):
            rem=copy%10
            sum+=(rem*rem*rem)
            copy//=10
        if(sum==num):
            print("armstrong no is:",num)
            num=num+1
#driver code
l=int(input("enter lower limit:"))  
u=int(input("enter upper limit:"))           
range_Armstrong(l,u)                    
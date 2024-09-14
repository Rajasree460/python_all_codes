def compound_interest(principal, rate, time):
 # Calculates compound interest
 amount = principal * (pow((1 + rate / 100), time))
 CI = int(amount-principal)
 print("Compound interest is", CI)
# Driver Code
p=int(input("enter the main amount:"))
q=int(input("enter the rate of interest:"))
r=int(input("enter the time:"))
compound_interest(p,q,r)
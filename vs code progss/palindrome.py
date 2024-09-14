#palindrome
n=122
rev=0
k=n
while n!=0:
    rem=n%10
    rev=rev*10+rem
    n=n/10
if k==rev:
   print('palindrome')
else:
    print('not palindrome')  
from pylab import *

i=input("Enter a number")
n=int(i)

while n!=1:
    if(n%2==0):
        n=n/2
        print(n)
    else:
        n=n*3+1
        print(n)
    

from pylab import *
#from _future_ import *

a,b=0,1
while b< 30:
    print(b,end=' ')
    c=a+b;
    a=b
    b=c
    
print()
a,b=0,1
while b< 30:
    print(b)
    a,b=b,a+b
 
n=int(input())
a,b=1,0  
for i in range(n):
    print(b,end=' ')
    c=a+b;
    a=b
    b=c
    
a,b=1,0  
for i in range(500):
    if (b%4==0 and b>8 and b<500):
        print(b,end=' ')
        break
    c=a+b
    a=b
    b=c  


    

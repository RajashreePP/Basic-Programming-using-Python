from pylab import *

#Multiplication table

n=int(input())

for i in range(1,11):
    print(n,"X",i,"=",n*i)
   
print()
     
for i in range(1,n+1):
    print(i)


#matrix

n=int(input())

for i in range(0,n):
    for j in range(0,n):
        print(i+j,end=' ')
    print()
    


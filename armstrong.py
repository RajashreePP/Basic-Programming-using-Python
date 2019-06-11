from pylab import *

r=input("Enter a number : ")
n=str(r)
l=len(n)
sum=0
for i in n:
    k=int(i)
    sum=sum+k**3

s=int(sum)
print(s)
if(s==r):
    print("Armstrong no.")
else:
    print("its not")

x=371
a=x//100
b=(x%100)//10
c=x%10

print((a**3+b**3+c**3)==x)

#Armstrong no. from 0 to 1000
x=100
while x<1000:
    a=x//100
    b=(x%100)//10
    c=x%10
    
    if((a**3+b**3+c**3)==x):
        print(x)


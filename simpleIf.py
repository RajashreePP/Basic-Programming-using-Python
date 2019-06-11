from pylab import *

i=input("Enter a number : ")
x=int(i)


if x<0:
    print('Negative of ',-(x))
elif x>0:
    print('Positive')
else:
    print('Zero')
    
print('Done')


x=int(input("Enter a number : "))
y=int(input())

if  x==y:
    print('same')
    highest=x
elif x>y:
    print('first')
    highest=x
else:
    print('second')
    highest=y

print(highest**2)

i=1
while i<=10:
    if(i%3==0):
        print('***')
    elif i%5==0:
        print('*****')
    else:
        print(i)
    i=i+1

#print * instead of numbers
i=1
while i<=10:
    print('*'*i)
    i+=1
    
    
  


    






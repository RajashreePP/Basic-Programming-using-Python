from numpy import *
x=linspace(0.0,10.0,200)
x *=2*pi/10
y=sin(x)
y=cos(x)
x[0]=-1
print(x[10],x[-1])

x=array([1.,2,3,4])
size(x)
x.dtype
x.shape
rank(x)
x.itemsize()

a=array([[0,1,2,3],[10,11,12,13]])
a.shape
a[1,3]
a[1,3]=-1
a[1]
a[1]=0

a=array([[1,2,3],[4,5,6],[7,8,9]])
a[0,1:3]
a[1:,1:]
a[:,2]

b=array([1,2,3,4,5,6])
b[1:3]



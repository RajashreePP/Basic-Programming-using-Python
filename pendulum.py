from pylab import *

x=loadtxt('pendulum.txt')
x.shape

x,y=loadtxt('pendulum.txt',unpack=True)
x.shape

plot(x,y)

clf()
L,t=loadtxt('pendulum.txt',unpack=True)
plot(L,t*t,'.')

a=imread('lena.png')
imshow(a)

show()
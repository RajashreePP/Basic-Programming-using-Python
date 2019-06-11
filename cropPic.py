from pylab import *

a=imread('lena.png')
imshow(a)

clf()
print(a.shape)
b=a[200:400,100:350]
print(b.shape)
imshow(b)

clf()

b=a[::2,::2]
print(b.shape)
imshow(b)

show()
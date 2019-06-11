from pylab import *

#printing numbers from 0 to 1 for n inputs

n=int(input())
dx=1.0/(n-1)
x=0.0
while x<(1.0-dx/2):
    print(x)
    x+=dx
print(1.0)

#OR
import numpy as np
print(np.linspace(0,1,n))



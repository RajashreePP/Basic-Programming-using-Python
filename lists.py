from pylab import *

n=[1,2,3,4,5]

print(n+[5,7,8])

n.append([5,7,8])
print(n)

n.extend([5,7,8])
print(n)

n.reverse() #first sorts it then reverses it
print(n)

n.remove(5) #removing specific element
print(n)

print(n.count(5))

print(n.index(3))

l=[3,6,2,1,4,]
l.sort()
print(l)

print(sorted(l,reverse=True))

print(1 in n)

print(2 not in n)




print(n)

del n[1] #removing by index






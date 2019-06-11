from pylab import *

time=[0.,1.,2,3]
distance=[7.,11,15,19]
plot(time,distance)
xlabel('time')
ylabel('distance')

clf()
plot(time,distance,'o')

clf()
plot(time,distance,'o')
plot(time,distance,'--')

mtlist=[]
p=[2,3,5,7]
print(p[1])
print(p[0]+p[1]+p[-1])
print(p[1:3])
print(p[::3])
print(p[::-1]) 
print(p[1:-1:2])

L=[0.2,0.3,0.4,0.5,0.6,0.7,0.8]
t=[0.90,1.19,1.30,1.47,1.58,1.77,1.83]


tsq=[]

for time in t:
    tsq.append(time*time)

print(len(L),len(t),len(tsq))

clf()
plot(L,tsq)




def sqr(arr):
    r=[]
    for x in arr:
        r.append(x*x)
    return r
    
tsq=sqr(t)


t=array(t)
tsq=t*t
print(tsq)

t=range(1000000)
tsq=sqr(t)



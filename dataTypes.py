from pylab import *

a=13
b=99999999999999
p=3.1423456
c=3+4j
c=complex(3,4)
t=True
F=not t
print(F and t)
print(F or t)


a=False
b=True
c=True

print(a and b or c)
print(a and b or c)

#String
s='This is string'
print(s)
s="This is string"
print(s)
s="""This is string
String are immutable
not changable"""
print(s)
s='''This is string'''
print(s)
print(len(s))
print(s[0],s[5],s[8])

print(type(s))

a=10
print(type(a))

b=5.7
print(type(b))

c=1+4j
print(type(c))

print(1786%12)


# ** is power operator
big=876543456789**4 
print(big)

verybig=big*big*big
print(verybig)

print(17/2)

print(17//2)

print(17.5/2)

print(17.5//2)

c=3+4j
print(abs(c))
print(c.imag)
print(c.real)

a=2344
a+=1
print(a)

#String operator
a='Rajshri '
p='Patil'

print(a+p)
print(a*5)
print(a.startswith('raj'))
print(a.endswith('ri '))
print(a.upper())
print(a.lower())

s='  hello world    '
print(s)
print(s.strip())
print(s.index('ll'))
print(s.replace('hello','hi'))
print(s)

#Split and join
c='a b c'
print(c.split())
print(c.join(['a','b']))

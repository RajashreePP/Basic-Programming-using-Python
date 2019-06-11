from pylab import *


ns=input("enter name : ")
print("Welcome",ns)
print(ns.upper())


n=input("Enter a int : ")
x=int(n)
sq=x*x
s=str(sq)
print(len(s))


a=input("Enter a complex no : ")
print(a)
c=complex(a)
print(c.real,c.imag)
print(abs(c))
print(c.conjugate())


from __future__ import print_function

f=open('new.txt','w')
print('hello',file=f)
f.close()

l="parse this        string"
print(l.split())

r='A;010001;ABINESH T N;053;036;28;16;44;177;;;'
print(r.split(';'))


s=open('pendulum.txt')
f=open('col2.txt','w')
for l in s:
    fl=l.split()
    print(fl[1],file=f)
s.close()
f.close()








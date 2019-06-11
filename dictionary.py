from pylab import *

d={'1':'one','2':'two','3':'three','4':'four'}

print(d)

print(d.keys())
print(d.values())

print(d.get('1'))

print(d.items())

d.update({'5':'five'})
print(d)

#another format
c=dict(a='one',b='two',c='three')

#finding duplicates
stud=dict(mayur='99',chaitu='95',tanu='99')
allM=list(stud.values())
unq=set(allM)
n_dups=len(allM)-len(unq)
print(n_dups,'Duplicates')












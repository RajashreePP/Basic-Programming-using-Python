from pylab import *

s=input("Enter a string : ")
print(s[1:])
print(s[:-1])
print(s[::-1])
print(s[::2])

#str.TAB to find the functions related to string

print(s.rfind('a'))

f=input("Enter a fileneame: ")
print(f+'.txt')

#takes list of fruits separated by , from user and print it
f=input("Enter fruits: ")

f=f.split(sep=',')
for i in f:
    print(i)
    
    
#print each character in string on new line
s=input("Enter a string")
for char in s:
    print(char)
    
    
from pylab import *

def sum(a,b):
    return a+b
    
#returning 2 values

def some():
    return 2,3
    
#default par (first parameter cant be a default par)
    
def wc(greet,name="world"):
    print(greet,name)

#function calling
wc("hi",name="rik")
hi rik

wc(name="rik",greet="gm")
gm rik

wc(name="rik","gm")
  File "<ipython-input-18-ada7fa493f59>", line 1
    wc(name="rik","gm")
                 ^
SyntaxError: positional argument follows keyword argument


    
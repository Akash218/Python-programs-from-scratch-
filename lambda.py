#user defined lambda fuction
'''def func(x):
    return(lambda y:x+y)
t=func(4)
print(t(12))'''
#lambda fuctions

'''a=[1,2,3,4,5,6,7,8]
b=list(map(lambda b:(b/3==2),a))
print(b)

import functools
d=functools.reduce(lambda c,b:c+b,a)
print(d)'''

#map-reduce functions
'''def new(a,b):
    return a**b
x=map(new,[1,2,3,4],[2,2,2,2])
print(list(x))'''

'''def new(i):
    if i>=3:
        return i
j=filter(new,(1,2,3,4,5,6,7,8,9))
print(list(j))'''
'''from functools import reduce
def redu(a,b):
    return a+b
c=reduce(redu,((1,2,3,4,5,6,7,8)))
print(c)'''
#linear equations and quadratic equations
'''a=lambda x,y:(((4*x)**2)+((7*y)**2))
print(a(2,5))'''
'''from functools import reduce
a=[1,2,3,4,5,6,7,8,9]
b=reduce(lambda x,y:x+y,map(lambda x:x+x,filter(lambda x:x<=4,a)))
print(b)'''



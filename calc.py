#pallindrom
def pal(n):
    a=n[::-1]
    if a==n:
        return'pallindrom'
    else:
        return 'not'
#factorial
def fact(n):
    if n==1 or n==0:
        return 1
    else:
        return n*fact(n-1)

#arithmatic operators
def add(a,b):
    return a+b
def sub(a,b):
    return a-b
def div(a,b):
    return a/b
def mul(a,b):
    return a*b
def expo(a,b):
    return a**b
def fd(a,b):
    return a//b



x=int(input('enter val:'))
y=int(input('enter val:'))
def decrator(func):
    def wrapper(a,b):
        print('the sum is:',a+b)
        func(x,y)
    return wrapper(x,y)
@decrator
def func2(a,b):
    print('the difference is:',a-b)


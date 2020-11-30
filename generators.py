'''def new(dict):
    for x,y in dict.items():
        yield x,y
a={1:'hi',2:'welcome'}
b=new(a)
print(next(b))
print(next(b)'''
#fibnocci series
'''def fib():
    f,s=0,1
    while True:
        yield f
        f,s=s,f+s
for x in fib():
    if x>50:
        break
        print(x,end='')'''

'''a=range(20)
b=(x for x in a)
print(b)
for y in b:
    print(y)

i=range(20)
for j in i:
    print(j)'''

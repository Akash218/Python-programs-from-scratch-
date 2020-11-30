
'''a=int(input())
b=[]
c=[]
for i in range(0,a):
    name = str(input())
    score =float(input())
    b.append(name)
    c.append(score)
k=dict(zip(b,c))
print(k)
m=set(c)
print('sets:',m)
n=list(m)
print('new list:',n)
y=sorted(n)
print('sorted:',y)
g=y[1]
print(g)
v=[q for q,w in k.items() if w==g]
print(v)
'''
'''from functools import reduce
n = int(input())
student_marks = {}
for i in range(n):
    name, *line = input().split()
    scores = list(map(float, line))
    student_marks[name] = scores
query_name = input()
a=student_marks[query_name]
b=reduce(lambda x,y:x+y,a)
c=b/len(a)
print(c)'''

'''a=int(input())
b=[]
for j in range(a):
    c=input().split()
    for i in range(1,len(c)):
        c[i]
    if c[0]=='insert':
        b.insert(int(c[1]),int(c[2]))
    elif c[0]=='append':
        b.append(int(c[1]))
    elif c[0]=='print':
        print(b)
    elif c[0]=='remove':
        b.remove(int(c[1]))
    elif c[0]=='pop':
        b.pop()
    elif c[0]=='sort':
        b.sort()
    elif c[0]=='reverse':
        b.sort(reverse=True)
    else:
        break'''

import _datetime
for i in range(int(input())):
    t1=_datetime.datetime.strptime(input(),'%a%d%b%Y%H%M%S%z')
    t2=_datetime.datetime.strptime(input(),'%a%d%b%Y%H%M%S%z')
print(abs(int((t1-t2).total_seconds())))




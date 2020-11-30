a=[3,6,9,12,15,18,21,24,27,30]
questiont=[]
for x in a:
    questiont.append(x*3)
print(questiont)

c=[x*3 for x in a]
print(c)

d=map(lambda y:y*3,a)
print(list(d))

from operator import add
a=[1,2,3,4,5]
b=[4,5,6,7,8]
print([sum(i) for i in zip(a,b)])
print(list(map(add,a,b)))
c=[a[i]+b[i] for i in range(len(a))]
print(c)
d=[]
for i in range(len(a)):
    d.append(a[i]+b[i])
print(d)

"""a='string'
print(a)
print(a[2])
print(len(a))
print(a.upper())
print(a.lower())
print(type(a))
b=sorted(a)
print(b)
print(''.join(b))
print(a[1:3])"""

#list
'''import collections
mylist=[2,3,4,5,'akash','is','a','python','developer']
mylist.insert(7,'wonderful')
mylist.append('and')
mylist.append('also he is good at web developing')
mylist[7]='awsome'
print(mylist)
mylist.pop(2)
print(mylist)
mylist.remove('and')
print(mylist)
del mylist[2]
print(mylist)
b=mylist.copy()
print(b)'''

#dictionary
'''a={'name':'akash','age':21,'gender':'male','role':'software developer'}
a['father name']='nallathambi'
print(a)
a['age']=22
print(a)
for x in a.keys():
    print(x)
for i in a.values():
    print(i)
for z,d in a.items():
    print(z,':',d)
if 'name' in a:
    print('yes')
a.pop('age')
print(a)
del a['gender']
print(a)
a.popitem()
print(a)

dict={'family 1':{'father':'nallathambi','mother':'alamelu','brother':'ajith kumar'},'family 2':{'uncle':'venkatesh','aunty':'selvi','grandma':'jothi','grandpa':'krishnamoorthy','uncle son1':'sriram','uncle son2':'dharsan'}}
print(dict)
for p in dict:
    print(p)'''
#tuples

'''tupl=(1,2,3,'banu','is','my','cousin',3,4,4,4,5,6)
print(tupl.count(3))
print(tupl.index('banu'))
print(tupl[5])

tupl1=list(tupl)
tupl1.append('akash')
tupl2=tuple(tupl1)
print(tupl2)

for j in tupl:
    print(j)
if 'banu' in tupl:
    print('yes')

tupl3=('i','love','my','mom')
tupl4=tupl+tupl3
print(tupl4)'''

#sets
'''sets={1,1,2,3,4,4,4,5,6,77,8,9,0}
set1={3,6,7,8,9,11,12,12,14}
sets.update(set1)
print(sets)
set3=sets.union(set1)
print(set3)
sets.update(['akash','is','a','man'])
print(sets)
sets.add(1656)
print(sets)'''
#collections in python

'''import collections
a=collections.namedtuple('courses','name,tech')
b=a('data science','python')
print(b)

d=[3,4,5,6,7,8]
c=collections.deque(d)
c.extend([1,2,3])
print(c)

e={'hi':'akash','how':'fine'}
f={'friend':'kalki','course':'ece'}
g=collections.ChainMap(e,f)
h=(e,f)
print(h)
print(g)

i=collections.Counter(c)
print(i.most_common())
sub={3:1}
i.subtract(sub)
print(i)

j=collections.OrderedDict()
j[1]='a'
j[2]='k'
j[3]='a'
j[4]='s'
j[5]='h'
print(j)

for k in j.items():
    print(k)

l=collections.defaultdict(int)
l[1]='akash'
l[2]='ajith'
l[3]='bharathi'
print(l[4])

m=collections.UserList(c)
print(m)'''




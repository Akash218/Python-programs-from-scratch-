from collections import namedtuple,deque,Counter,ChainMap,OrderedDict,defaultdict
a=namedtuple('courses','python,java,c,linux')
b=a('django','angularjs','embed','os')
print(b)

c=[1,1,2,3,4,2,3,4,5,5,6,7,8,1,9,10,12,5,6,7,8,9,10,11,12,13,14,15]
d=deque(c)
d.popleft()
d.appendleft(0)
d.insert(1,1)
print(d)

e=Counter(c)
print(e)
print(list(e.elements()))
print(e.most_common())
sub={5:2,12:1}
e.subtract(sub)
print(e)

f=OrderedDict()
f[0]='a'
f[1]='n'
f[2]='u'
print(f)

from array import array as arr
a=arr('i',[1,2,3,4,5,6])
b=arr('i',[6,7,8,9,10,11])
print(a+b)
print(a[1:4])
a.append(12)
a.extend([13,14,15])
a.insert(10,16)
b.pop(4)
b.remove(6)
print(a)
print(b)
c=a[::-1]
print(c)
for a in c:
    print(a)
a=0
while a<len(c):
    print(c[a])
    a+=1


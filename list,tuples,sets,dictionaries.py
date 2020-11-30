#list
fruits=['apple','banana','grapes','mango','pineapple','strawberry']
print(fruits[2:4])
print(fruits.append('kiwi'))
print(fruits.insert(3,'jack fruit'))
print(fruits.pop(3))
print(fruits.remove('banana'))
del fruits[4]
fruits[2]='oronge'
print(len(fruits))

#tuple
even=(2,4,6,8,4,10,12,4)
print(even.count(4))
change_to_list=list(even)
change_to_list[5]=20
change_to_tuple=tuple(change_to_list)
print(change_to_tuple)
print(len(even))


#dictionary
students={'names':['aravind','anoop','arjun','bala','kalki','vishnu','chandru','kamesh','krishna','jerold','ashok'],'marks in english':[78,82,76,92,88,86,77,68,65,95,79],'marks in tamil':[86,77,68,65,95,92,88,86,77,68,90],'matrks in maths':[79,80,90,82,83,65,95,92,88,86,77],'marks in science':[76,88,87,69,70,79,80,90,82,83,65],'marks in social':[88,87,89,90,91,87,69,70,79,80,90]}
students.pop('names')
del students['marks in english']
students['marks in practical']=[78, 82, 76, 92, 88,76, 92, 88, 86, 77, 68]
print(students)
for x,y in students.items():
    print(x,y)
for x in students.keys():
    print(x)
for y in students.values():
    print(y)


#sets
a=set(range(10))
a.update([4,3,5,4,3,6,10,24,13])  #inside the set bracket no duplicate values are emerged
b={11,12,13,14,15,16}
c=a.union(b)
print(c)
d=set(range(30,36))
d.update(c)
print(d)
d.add(100)
print(d)
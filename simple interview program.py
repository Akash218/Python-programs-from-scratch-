#pallindrom
#method 1
'''def pal(string):
    if string==string[::-1]:
        print('pallindrom')
    else:
        print('not a pallindrom')
pal(input('enter a string:'))'''

#method 2
'''a=input()
b=''
for i in a:
    b=i+b
if a==b:
    print('yes')
else:
    print('no')'''

#method 3
'''a=input('enter string value:')
rev=''.join(reversed(a))
if a==rev:
    print('yes')
else:
    print('no')'''






#factorial

'''a=int(input('enter a value:'))
factorial=1
if a==0 or a==1:
    print('The factorial of {} is 1'.format(a))
else:
    for i in range(1,a+1):
        factorial=factorial*i
    print('The factorial of {} is {}'.format(a,factorial))'''

#accending order
#method 1(build in method)
'''
list=[5,9,4,6,3,7,2]
print(sorted(list))

#method 2
list=[5,9,4,6,3,7,2]
for i in range(0,len(list)):
    for j in range(i+1,len(list)):
        if list[i]>list[j]:
            temp=list[i]
            list[i]=list[j]
            list[j]=temp
print(list)
'''
# method 3
'''list=[5,9,4,6,3,7,2]
a=[]
while list:
    minimum=list[0]
    for i in list:
        if i<minimum:
            minimum=i
    a.append(minimum)
    list.remove(minimum)
print(a)'''



















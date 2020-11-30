'''from functools import reduce
a=[1,2,3,4,5,6,7,8]
b=list(map(lambda x:x>3,a))
print(b)
c=list(filter(lambda x:x>3,a))
print(c)
d=reduce(lambda x,y:x+y,a)
print(d)
e=reduce(lambda x,y:x+y,map(lambda x:x+3,filter(lambda x:x>3,a)))
print(e)

quadratic_equation=lambda x,y:(x**2)+(y**2)
print(quadratic_equation(3,4))

def linear_equation(o,p):
    print(lambda o,p:(3*o)+(4*p))
linear_equation(2,2)

l=[5,6,4,3,7,8,1,9,12,43,21]
print(l.sort())'''
from functools import reduce
restart=('Y')
while restart not in ('n','N','no','NO'):
    print('1.Detect if the given number is octal number')
    print('2.pass and sum the list to the method and return value')
    print('3.check the number is less than 10')
    print('4.exit the menu')
    menu=int(input('enter your choice:'))
    if menu==1:
        try:
            num=int(input("enter octal number:"),8)
            print("num(decimal format):",num)
            print("num(octal format):",oct(num))
        except ValueError:
            print("Plese enter only Octal Value")
        restart='Y'
    elif menu==2:
        def my_function(numbers):
            for x in numbers:
                print(x)


        inputs=list(input('enter sequence of numbers').split())
        my_function(inputs)
        print('sum of numbers:',reduce(lambda x,y:x+y,inputs))
        restart = 'Y'
    elif menu==3:
        input=list(input('enter sequence of numbers').split())
        print(input)
        restart = 'Y'
    elif menu==4:
        print('Thank You')
        break










'''try:
    print(10/100)
except ArithmeticError:
    print('Oops! can not be divide any number by zero')'''

'''def fact(n):
    if n==1:
        return n
    else:
        return n*fact(n-1)
print(fact(-4))'''


'''def fact(n):
    if n == 1:
        return n
    else:
        try:
            return n * fact(n - 1)
        except ValueError:
            print('negative number can not be print')
        except:
            print('error occured')
print(fact(-2))'''

#input a is any number
#input b is 0 0r any number
a=int(input('enter a number:'))
b=int(input('enter a number:'))
try:
    if a/b:
        print('A is divisible by b,value is',a/b)
except:
    print('NO values are divisible by zero, it leads to infinity')
else:
    print('work done')
finally:
    print('Thank You')

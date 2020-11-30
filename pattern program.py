#Diamond Pattern
'''def pattern(n):
    k=(2*n)-2
    for i in range(0,n):
        for j in range(0,k):
            print('',end=' ')
        k=k-1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    for i in range(n-2,-1,-1):
        for j in range(k+2,0,-1):
            print('',end=' ')
        k=k+1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(5)'''

'''
#Glass Hour Pattern

def pattern(n):
    k=(2*n)-2
    for i in range(n-1,-1,-1):
        for j in range(k+1,0,-1):
            print('',end=' ')
        k=k+1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
    for i in range(0,n):
        for j in range(0,k):
            print('',end=' ')
        k=k-1
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(5)'''

#Right angle pattern
def pattern(n):
    for i in range(0,n):
        for j in range(0,i+1):
            print('* ',end='')
        print('\r')
pattern(5)



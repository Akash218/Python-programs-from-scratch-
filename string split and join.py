#examble
'''a='akash is a son of nallathambi'
a=a.split(' ')
print(a)
a='-'.join(a)
print(a)'''

def split_and_join(line):
    a=line.split(' ')
    a="-".join(a)
    return a
b=input()
print(split_and_join(b))

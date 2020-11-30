#method 1
import textwrap
b='abcdefghijklmnopqrstuvwxyz'
a=textwrap.wrap(b,5)
for i in a:
    print(i)

#method 2
a=textwrap.fill('abcdefghijklmnop',3)
print(a)
import random
a=input('enter your password:')
b=[]
for i in range(97,123):
    b.append(chr(i))
guess=''
while(guess!=a):
    guess=''
    for x in range(len(a)):
        guess_letter=b[random.randint(0,25)]
        guess=str(guess_letter)+str(guess)
    print(guess)
print('your password is',guess)



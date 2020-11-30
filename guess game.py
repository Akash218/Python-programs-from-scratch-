from random import randint
random_guess = randint(1,21)
attempts=0
while True:
    attempts+=1
    guess = int(input('enter number between 20:'))
    if guess==random_guess and guess in range(1,21):
        print('WoW,YoU MadE It!!!\n','Number of attempts is:',attempts)
        break
    elif guess>random_guess and guess in range(1,21):
        print('your value is too big')
    elif guess<random_guess  and guess in range(1,21):
        print('your value is too low')
    else:
        print('enter valid number')

import random
list=['stone','paper','scissor']
points=0
game='c'
while game=='c':
    random_guess = random.choice(list)
    guess = input('enter stone or paper or scissor:')
    if guess in list:
        if guess==random_guess:
            print('your value is:',guess,'\n random value is:',random_guess)
            print('your point is',points)
            game=input('do u want to continue or quit, enter c or q:')
        elif guess=='stone' and random_guess=='paper':
            points-=1
            print('\n your value is:',guess,'\n random value is:',random_guess)
            print('you loose one point:\n','your point is:',points)
            game=input('do u want to continue or quit, enter c or q:')
        elif guess=='stone' and random_guess=='scissor':
            points+=1
            print('\n your value is:',guess,'\n random value is:',random_guess)
            print('you gain one point:\n','your point is:',points)
            game=input('do u want to continue or quit, enter c or q:')
        elif guess=='paper' and random_guess=='stone':
            points+=1
            print('\n your value is:',guess,'\n random value is:',random_guess)
            print('you gain one point:\n', 'your point is:', points)
            game=input('do u want to continue or quit, enter c or q:')
        elif guess=='paper' and random_guess=='scissor':
            points -= 1
            print('\n your value is:',guess,'\n random value is:',random_guess)
            print('you loose one point:\n', 'your point is:', points)
            game=input('do u want to continue or quit, enter c or q:')
        elif guess=='scissor' and random_guess=='stone':
            points -= 1
            print('\n your value is:',guess,'\n random value is:',random_guess)
            print('you loose one point:\n', 'your point is:', points)
            game=input('do u want to continue or quit, enter c or q:')
        elif guess=='scissor' and random_guess=='paper':
            points += 1
            print('\n your value is:',guess,'\n random value is:',random_guess)
            print('you gain one point:\n', 'your point is:', points)
            game = input('do u want to continue or quit, enter c or q:')
        else:
            print('empty value')
    else:
        print('enter valid option:?')
        game = input('do u want to continue or quit, enter c or q:')



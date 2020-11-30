

'''import random
computer_guess=int(random.randrange(20))+1
guess=0
while guess!=computer_guess:
    guess=int(input('enter number between 1 to 20:'))
    if guess>0:
        if guess>computer_guess:
            print('number is too large')
        elif guess<computer_guess:
            print('number is too small')
    else:
        print('sorry')
        break
else:
    print('congratulation')'''

'''print('welcome to iob')
restart='y'
chances=3
mybal=10000
while chances>=0:
    pin = int(input('enter your pin:'))
    if pin==(1234):
        print('you entered your pin correctly\n')
        while restart not in ('n','no','NO','N'):
            print('please press 1 for your balance:\n')
            print('please press 2 for withdraw:\n')
            print('please press 3 to pay in:\n')
            print('please press 4 to return card:\n')
            option=int(input('what would u like to choose?'))
            if option==1:
                print('your balance is :',mybal,'rs\n')
                restart=input('would u like to go back?')
                if restart in ('n','no','NO','N'):
                    print('thankyou')
                    break
            elif option==2:
                withdrawl=float(input('how much would you like to withdraw?\nrs100/rs200/rs500/rs1000/rs2000'))
                if withdrawl in [100,200,500,1000,2000]:
                    mybal=mybal-withdrawl
                    print('your current balance is:',mybal)
                    restart = input('would u like to go back?')
                    if restart in ('n', 'no', 'NO', 'N'):
                        print('thankyou')
                        break
                elif withdrawl != [100,200,500,1000,2000]:
                    print('invalid amount,please retry\n')
                    restart=('y')
                elif withdrawl==1:
                    withdrawl=float(input('please enter desired amount:'))

            elif option==3:
                pay_in=float(input('how much would you like to pay in?'))
                mybal=mybal+pay_in
                print('\nyour balanc is now rs',mybal)
                restart=input('would you like to go back?')
                if restart in ('n', 'no', 'NO', 'N'):
                    print('thankyou')
                    break

            elif option==4:
                print('please wait while your card is returned...\n')
                print('Thank you for your service')
                break

            else:
                print('please enter a crt number.\n')
                restart=('y')
    elif pin!=('1234'):
        print('incorrect password')
        chances=chances-1
        if chances==0:
            print('\nNo more tries')
            break'''




travelling=input('yes or no')
while travelling=='yes':
    num=int(input('number of people travelling'))
    for i in range(1,num+1):
        name=input('name:')
        age=input('age:')
        gender=input('male or female:')
        print(name)
        print(age)
        print(gender)
    travelling=input('oops! forgot someone')


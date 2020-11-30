pin=input('enter your pin:')
balance=10000
restart='n'
if pin=='1234':
    while restart!='y':
        print('do you want to withdraw your cash,press 1?')
        print('do you want to credit your cash,press 2? ')
        print('do you want to check your balance,press 3?')
        print('do you want to quit your process,press 4?')
        choice=int(input('enter your choice?'))
        if choice==1:
            input1=int(input('enter your amount:'))
            if input1>balance:
                print('')
                print('---------------------------------------------------')
                print('SORRY, your account does not has sufficiant balance')
                print('---------------------------------------------------')
            else:
                balance=balance-input1
                print('your current balance is:',balance)
            restart=input('do you want to quit,if yes press y or press n:')
        elif choice==2:
            input1 = int(input('enter your amount:'))
            balance = balance+input1
            print('your current balance is:', balance)
            restart = input('do you want to quit,if yes press y or press n:')
        elif choice==3:
            print('your balance is:',balance)
            restart = input('do you want to quit,if yes press y or press n:')
        elif choice==4:
            print('Thank You')
            break
else:
    print('enter valid pin?')
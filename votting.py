choose='yes'
pin_for_start_election='1234'
pin_for_page_access=5678
while True:
    election_pin = input('enter pin to start election or enter exit:')
    if election_pin==pin_for_start_election:
        count_for_DMK=0
        count_for_ADMK=0
        count_for_BJK=0
        count_for_PSK=0
        while choose=='yes':
            age=int(input('enter your age:'))
            if age>=18:
                print('vote for DMK,press 1')
                print('vote for ADMK,press 2')
                print('vote for BJK,press 3')
                print('vote for PSK,press 4')
                print('@@ press 5 to watch the result,only admin can do it with password @@')
                print('@@ press 6 t0 stop election,only admin can do it with password @@')
                print('')
                choice=int(input('enter your choice:'))
                if choice==1:
                    confirm=input('Do you want to confirm your vote for DMK,press enter or press any key to cancel:')
                    if confirm=='':
                        count_for_DMK+=1
                        print('')
                        print('---------')
                        print('THANK YOU')
                        print('---------')
                        print('')
                        continue
                    else:
                        print('')
                        print('## please select any one ##')
                        print('')
                        continue
                elif choice==2:
                    confirm=input('Do you want to confirm your vote for ADMK,press enter or press any key to cancel:')
                    if confirm=='':
                        count_for_ADMK+=1
                        print('')
                        print('---------')
                        print('THANK YOU')
                        print('---------')
                        print('')
                        continue
                    else:
                        print('')
                        print('## please select any one ##')
                        print('')
                        continue
                elif choice==3:
                    confirm=input('Do you want to confirm your vote for BJK,press enter or press any key to cancel:')
                    if confirm=='':
                        count_for_BJK+=1
                        print('')
                        print('---------')
                        print('THANK YOU')
                        print('---------')
                        print('')
                        continue
                    else:
                        print('')
                        print('## please select any one ##')
                        print('')
                        continue
                elif choice==4:
                    confirm=input('Do you want to confirm your vote for PSK,press enter or press any key to cancel:')
                    if confirm=='':
                        count_for_PSK+=1
                        print('')
                        print('---------')
                        print('THANK YOU')
                        print('---------')
                        print('')
                        continue
                    else:
                        print('')
                        print('##  please select any one ##')
                        print('')
                        continue
                elif choice==5:
                    password=int(input('please enter the password to access this page:'))
                    if password==pin_for_page_access:
                        print('')
                        print('-------------------------------------------------------')
                        print('Total number of votes received for DMK:',count_for_DMK)
                        print('Total number of votes received for ADMK:',count_for_ADMK)
                        print('Total number of votes received for BJK:',count_for_BJK)
                        print('Total number of votes received for PSK:',count_for_PSK)
                        print('------------------------------------------------------')
                        print('')
                        CONTINUE=input('press any key to continue the election')
                        if CONTINUE=='':
                            continue
                        else:
                            continue
                    else:
                        print('your password was wrong')
                        choose='yes'
                elif choice==6:
                    password = int(input('please enter the password to access this page:'))
                    if password == pin_for_page_access:
                        print('Total number of votes received for DMK:', count_for_DMK)
                        print('Total number of votes received for ADMK:', count_for_ADMK)
                        print('Total number of votes received for BJK:', count_for_BJK)
                        print('Total number of votes received for PSK:', count_for_PSK)
                        stop_election=input('Do you want to stop the election,enter the election password:')
                        if stop_election==pin_for_start_election:
                            print('***********************************************')
                            print('THANK YOU FOR ALL PARTICIPATING IN THE ELECTION')
                            print('***********************************************')
                            break
                        else:
                            print('election password was wrong')
                            continue
                    else:
                        print('your password was wrong')
                        continue
                else:
                    print('please enter valid number?')
                    continue
            else:
                print('you are not eligible for voting')
    elif election_pin=='exit':
        break
    else:
        print('please enter the correct password')
        continue
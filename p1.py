dic = {}
while True:
    amount = 0
    print('--------Menu--------')
    print('1. Open a savings account')
    print('2. Deposit Money')
    print('3. Withdraw Money')
    print('4. Enter Details and Deposit Amount')
    print('5. Exit')
    choice = int(input('Enter your choice: '))
    if choice == 5:
        break
    elif choice == 1:
        name = input('Enter your name: ')
        print('Deposit Minimum Amount!')
        amount += int(input('Deposit:'))
        dic[name] = amount
    elif choice == 2:
        name = input('Enter your name: ')
        if name in dic.keys():
            dic[keys] += int(input('Enter amount: '))
        else:
            print('create an account first')
    elif choice == 3:
        name = input('Enter your name: ')
        if name in dic.keys():
            dic[keys] -= int(input('Enter amount: ')        
        else:            
            print('create an account first')

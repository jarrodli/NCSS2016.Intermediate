def blood_work(a, b, c, d):

    if a.lower() == c.lower():
        if b == '-' and d == '-':
            print('Match!')
        elif b == '-' and d == '+':
            print('Match!')
        elif b == '+' and d == '+':
            print('Match!')
        else:
            print('Rh factor does not match.')

    elif a.lower() in c.lower():
        if b == '-' and d == '-':
            print('Match!')
        elif b == '-' and d == '+':
            print('Match!')
        elif b == '+' and d == '+':
            print('Match!')
        else:
            print('Rh factor does not match.')

    elif a.lower() == 'o':
        if b == '-' and d == '-':
            print('Match!')
        elif b == '-' and d == '+':
            print('Match!')
        elif b == '+' and d == '+':
            print('Match!')
        else:
            print('Rh factor does not match.')

    elif a.lower() != c.lower():
        if b == '-' and d == '-':
            print('Blood group does not match.')
        elif b == '-' and d == '+':
            print('Blood group does not match.')
        elif b == '+' and d == '+':
            print('Blood group does not match.')
        else:
            print('Both blood group and Rh factor do not match.')


blood_work(input('Donor blood group: '), input('Donor Rh factor: '), input('Recipient blood group: '), input('Recipient Rh factor: '))

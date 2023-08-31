def calculator():
    print('What operation do you want to carry out, (+, -, /, *)')
    calculation = input()
    if calculation == '+':
        print('Enter the two values to be computerd')
        x1 = int(input())
        x2 = int(input())
        total = x1 + x2
        print(total)

calculator()

''' elif calculation == '-':
        print('Enter the two values to be computerd')
        x1, x2 = input(x1, x2)
        total = x1 - x2
        print(total)
    elif calculation == '/':
        print('Enter the two values to be computerd')
        x1, x2 = input(x1, x2)
        total = x1 / x2
        print(total)
    elif calculation == '*':
        print('Enter the two values to be computerd')
        x1, x2 = input(x1, x2)
        total = x1 * x2
        print(total)
    else:
        print('You have entered an incorrect value, please try again later')


calculator()
'''
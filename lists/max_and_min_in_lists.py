all_numbers = []

while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        all_numbers.append(number)
    except ValueError:
        print('Error!! Enter a numeric type')
    except TypeError:
        print('Error!! Try again')

maximum = max(all_numbers)
minimum = min(all_numbers)

print('The maximum is:', maximum, 'and the minimum is:', minimum)

all_numbers = []

while True:
    try:
        number = input('Enter a number: ')
        if number == 'done':
            break
        all_numbers.append(number)
    except:
        print('Enter a numeric type')

maximum = max(all_numbers)
minimum = min(all_numbers)

print('The maximum is:', maximum, 'and the minimum is:', minimum)

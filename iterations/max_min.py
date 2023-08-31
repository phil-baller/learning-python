def get_max_number(all_numbers):
    max = None
    min = None
    for v in all_numbers:
        if max is None or v > max:
            max = v
        if min is None or v < max:
            min = v    
    print('The maximum and minimum numbers are:', max, min)

all_numbers = []
while True:
    print("Enter some numbers")
    number = input()
    try:
        if number == 'done':
            break
        add_to_list = all_numbers.append(int(number))
    except ValueError:
        print("Enter a numeric value")
    except TypeError:
        print("Bad data, enter a numric value") 
print("DONE!")

get_max_number(all_numbers)
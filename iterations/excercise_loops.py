iterateGlobal = 0
countGlobal = 0

def total_numbers(all_numbers):
    count = 0
    for i in all_numbers:
        count = count + i
    print("The total of the numbers is:", int(count))
    return count

def get_max_number(all_numbers):
    max = None
    for v in all_numbers:
        if max is None or v > max:
            max = v
    print('The maximum number is:', max)

def count_numbers(all_numbers):
    iterate = 0
    for new in all_numbers:
        iterate = iterate + 1
    print("There are", iterate, "numbers in the list")
    return iterate

def average_numbers(count, iterate):
    final_average = count/iterate
    print("The average of all the numbers is:", final_average)

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
        print("Please enter a numeric value") 
print("DONE!")

print(all_numbers)
countGlobal = total_numbers(all_numbers)
get_max_number(all_numbers)
iterateGlobal = count_numbers(all_numbers)
average_numbers(countGlobal, iterateGlobal)
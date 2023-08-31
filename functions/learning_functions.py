import math
import random


def all_numbers(max):
    total = []
    for v in range(max):
        count = int(random.randrange(max))
        final = total.append(count)
    print(total)


print('Enter a number between 5 - 40')
number = int(input())

all_numbers(number)




import math

print('Enter any number of your choice')
number = int(input())

conversion = math.sin(number)
conversion_1 = math.log10(number)
conversion_3 = math.log(number)

print(conversion, conversion_1, conversion_3)
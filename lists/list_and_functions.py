''' list = [2, 34, 65, 56, 43, 98]

print(len(list))
print(sum(list))
print(min(list))
print(max(list))
print(sort(list))
'''
# Avoid using the keyword list() as a variable given that it's a reserved keyword
elements = list()
count = 0

while True:
    value = input('Enter values: ')
    if value == 'done':
        break
    numbers = float(value)
    add_to_list = elements.append(numbers)
    count = count + 1

print(elements)
print("The sum of the list is: ", sum(elements))
print("The average of list is", sum(elements)/count)
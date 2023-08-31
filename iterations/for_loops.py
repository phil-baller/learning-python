'''
friends = ['john', 'Joshua', 'Samuel', 'Jane']

for friend in friends:
    print('Happy New year:', friend)
    if friend is 'Joshua':
        print('Joshua you\'ve always been my favorite')
'''
'''
# Counting elements in a list
numbers = [3, 43, 56, 45, 76, 34, 786, 23, 56]

count = 0
for i in numbers:
    count = count + i

print('The sum of the list is equal to: ', count)
'''

# Finding the largest element in a list
largest = None
print('Before:', largest)
for intervar in [3, 41, 12, 9, 74, 15]:
    if largest is None or intervar > largest:
        largest = intervar
    print("Loop:", intervar, largest)
print('Largest:', largest)



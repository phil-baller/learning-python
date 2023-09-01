'''elements = ['a', 'b', 'c', 'd', 'e', 'f']

new_list = elements[1:5]

new_list[1:] = ['df', 'sds', 'sdf']
print(new_list)
'''

''' elements = ['g', 'z', 'c', 'a', 'e', 'k']
second_elements = ['New', 'better', 'without']

print(max(elements))
print(min(elements))
#print(sum(elements))

print(elements)
'''

test = 'This is a basic sentence'

x = list(test)

count = 0
for v in x:
    count = count + 1

print('There are: ',  count)
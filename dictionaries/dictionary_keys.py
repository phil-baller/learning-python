information = open('../romeo.txt')

keys = {}
#delimiter = ' '
for v in information:
    data = v.split()
    for x in data:
        if x not in keys:
            keys[(x)] = 1
        else:
            keys[(x)] += 1

for lines in keys:
    print(lines, keys[lines])

'''
get_file = input('Enter the name of a file: ')

try:
    open_file = open(get_file)
except:
    print('File not found!! Check Name')
    exit()

counts = dict()
for x in open_file:
    break_file = x.split()
    for z in break_file:
        if z not in counts:
            counts[z] = 1
        else:
            counts[z] += 1

print(counts)
'''





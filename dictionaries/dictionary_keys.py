information = open('words.txt')

keys = {}
delimiter = ' '
for v in information:
    data = v.split(delimiter)
    for x in data:
        if x not in keys:
            keys[(x)] = " "

print(keys)
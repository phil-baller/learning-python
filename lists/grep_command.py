import re

command = input('Enter the command: ')
data = open('mbox.txt')

count = 0
for lines in data:
    lines = lines.rstrip()
    x = re.findall(command, lines)
    if len(x) > 0:
        count += 1

print('There are', count, 'words that matched', command)
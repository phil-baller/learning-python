opening = open('mbox.txt', 'r')
new_file = open('everything.txt', 'w')
'''
for all in opening:
    if all.startswith('From:'):
        new_file.write(all)
'''
count = 0
for all in opening:
    if all.startswith('Subject'):
        count = count + 1

print('There are', count, 'words called complete')

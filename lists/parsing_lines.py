from prettytable import PrettyTable

document = open('mbox-short.txt')

count = 0
mail = date = time = list()
for file in document:
    concat = file.rstrip()
    if not file.startswith('From '):
        continue 
    words = concat.split()
    amount = words[2:5]
    delimiter = ' '
    joined = delimiter.join(amount)

    t = PrettyTable(['Email Address', 'Date', 'Time'])
    t.add_row([words[1], joined, words[5]])
    print(t)
    
    
'''
for v in mail:
    print(v)
t = PrettyTable(['Email Address', 'Time'])

for v in range(count):
    t.add_row(mail, date, time)

print(t)

for v in mail:
    print(v,'\t')
'''    

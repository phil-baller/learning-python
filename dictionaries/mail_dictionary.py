file_name = input('Enter the name of the file: ')

try:
    file_open = open(file_name)
except:
    print('File not found, try again')
    exit()

count = dict()
for lines in file_name:
    data = lines.strip()
    if lines.startswith('From '):
        data = lines.split()
        count[data[2]] = data[4]
        print(count) #Unfortunately, a dictionary can have only one unique key to itself

#uncomment line below for complete program run
"""for x in count:
    print(x, count[x])
"""


""" 
    for information in data:
        print(information)"""

'''for x in lines:
data = x.split()
print(data)'''
    

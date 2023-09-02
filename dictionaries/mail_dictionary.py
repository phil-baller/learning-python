file_name = input('Enter the name of the file: ')

try:
    file_open = open(file_name)
except:
    print('File not found, try again')
    exit()

count = dict()
for lines in file_open:
    #lines = lines.rstrip()
    if not lines.startswith('From '):
        continue
    for x in lines:
        data = x.split()
        print(data)
    

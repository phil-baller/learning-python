def finding_confidence(file_string):
    begin = file_string.find(':')
    stop = file_string.find('\'', begin)
    complete = file_string[begin + 1:stop]
    conversion = float(complete)
    return conversion

file_name = input('Enter the name of the file: ')
try:
    open_file = open(file_name)
except:
    print('Directory not found!! Check name and try again')
    exit()

count = 0
total = 0.0
for v in open_file:
    if v.startswith('X-DSPAM-Confidence: '):
        count = count + 1
        confidence_found = finding_confidence(v)
        print(confidence_found)
        total = total + confidence_found

average = total/count
print('Average spam confidence: ', average)
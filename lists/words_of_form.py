import re
data = open('mbox-short.txt')

iterate = 0
count = 0.0
for line in data:
    line = line.rstrip()
    y = re.findall('\S \S.+: ([0-9]+)', line)
    if len(y) > 0:
        y_string = y[0]
        y_float = float(y_string)
        count = count + y_float
        iterate += 1

average = count/iterate

print('Average: ',average)
  

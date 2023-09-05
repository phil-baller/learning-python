import re

data = open('mbox.txt')
count = {}
for lines in data:
    lines = lines.rstrip()
    x = re.findall('[a-zA-Z0-9]\S+@\S+[a-zA-Z]', lines)
    if len(x) > 0:
        print(x)
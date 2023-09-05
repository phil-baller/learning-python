import re

data = open('mbox-short.txt')

for lines in data:
    lines = lines.rstrip()
    x = re.findall('\S+@\S+', lines)
    if len(x) > 0:
        print(x)
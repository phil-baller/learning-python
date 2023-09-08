import re

fhand = open('../mbox-short.txt')
for v in fhand:
    v = v.rstrip()
    #if re.search('F..m:', v):
    if re.search('^F..m:.+@', v):
        print(v)
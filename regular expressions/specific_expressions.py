import re
import sys

new_file = open('new_domains.txt', 'w')
data = open('../mbox-short.txt')
list_of_emails = []
for lines in data:
    lines = lines.rstrip()
    x = re.findall(r'[a-zA-Z]\w+@[a-zA-Z]\w+', lines)
    if len(x) > 0 and x not in list_of_emails:
        list_of_emails.append(x)

for v in list_of_emails:
    new_file.write(v[0])
    new_file.write('\n')


"""if len(x) > 0 and x not in list_of_emails:
list_of_emails.append(x)

for v in list_of_emails:
    new_file.write('\n')
    new_file.write(v[0])"""


new_file.close()

"""if len(x) > 0:
print(x)"""

"""for lines in data:
    lines = lines.rstrip()
    x = re.findall('^X\S+: [0-9.]+', lines)
    if len(x) > 0:
        print(x)"""

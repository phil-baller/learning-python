import re
import sys

data = open('../mbox-short.txt')

for lines in data:
    lines = lines.rstrip()
    x = re.findall(r'Received:\s+\w+\s+([\S]+)', lines)
    if len(x) > 0:
        print(x)

    """if len(x) > 0:
        print(x)"""

"""for lines in data:
    lines = lines.rstrip()
    x = re.findall('^X\S+: [0-9.]+', lines)
    if len(x) > 0:
        print(x)"""

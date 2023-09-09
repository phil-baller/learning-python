import re

greedy_comparing = re.compile(r'(\d\d\d)-(\d\d\d)-(\d\d\d\d)')
final = greedy_comparing.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(final[0])

non_greedy_comparing = re.compile(r'\d\d\d-\d\d\d-\d\d\d\d')
total = non_greedy_comparing.findall('Cell: 415-555-9999 Work: 212-555-0000')
print(total)



import pyperclip, re

phone_pattern = re.compile(r'''(
    (\d{3}|\(\d{3}\))?      #area code
    (\s|-|\.)?              #separator
    (\d{3})                 #first 3 digits
    (\s|-|\.)               #separator
    (\d{4})                 #last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5})))?      #extension
    ''', re.VERBOSE)

email_pattern = re.compile(r'''
    [a-zA-Z0-9.%+-]+
    @
    [a-zA-Z0-9.-]+
    (\.[a-zA-Z]{2,4})
    ''', re.VERBOSE)

text = str(pyperclip.paste())
matches = []
for data in phone_pattern.findall(text):
    phone_Num = '-'.join([data[1], data[3], data[5]])
    if data[8] != ' ':
        phone_Num += ' x' + data[8]
        matches.append(phone_Num)
for data in email_pattern.findall(text):
    matches.append(data[0])


if len(data) > 0:
    pyperclip.copy('\n'.join(data))
    print('Copied to clipboard:')
    print('\n'.join(data))
else:
    print('No phone numbers or email addresses found.')
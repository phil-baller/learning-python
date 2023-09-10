import re

#Strong password detection program
upper_lower_case = re.compile(r'[a-zA-Z]')
one_digit = re.compile(r'[0-9]')
special = re.compile(r'[^a-zA-Z0-9]')

password = "Beatballer_22"#input('Enter your password: ')
new_upper = upper_lower_case.findall(password)
new_one = one_digit.findall(password)
new_special = special.findall(password)

print(str(new_upper))
print(str(new_one))
print(str(new_special))


"""if len(password) < len(new_char):
    print('You need to enter a long password')
elif str(new_upper) not in password:
    print('You need to use both upper and lowercase characters')
elif str(new_one) not in password:
    print('Your password needs atleast one numberic type')
elif str(new_special) not in password:
    print('Your password needs atleast one special character')
else:
    print('You have a strong password: %s' %password)"""


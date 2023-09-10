import re

#Strong password detection program
upper_lower_case = re.compile(r'[a-zA-Z]')
one_digit = re.compile(r'[0-9]')
special = re.compile(r'[^a-zA-Z0-9]')

while True:
  try:
    password = input('Enter your password: ')
    new_password = list(password)

    new_upper = upper_lower_case.search(password)
    new_one = one_digit.search(password)
    new_special = special.search(password)
    if len(password) < 8:
      print('Your password needs to be atleast 8 characters long')
    elif new_upper == None:
      print('Your password needs atleast an uppercase and a lowercase')
    elif new_one == None:
      print('Your password requires atleast one numric value')
    elif new_special == None:
      print('Your password requires atleast one special symbol')
    else:
      print('You have a strong password: %s' %password)
      break
  except:
    print('Your compiler has an error')



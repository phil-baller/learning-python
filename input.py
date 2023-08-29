print('Enter your Full Name')
username = input()

print('Enter your Password')
password = input()
 
if password == "Beatballer22":
    print('Your Password is', password)
else:
    print('Please try again!! - Wrong Password Entered')

print('Your username is', username,  "and password is",  password, "\n" "which is", str(len(password)) + " Characters long" )
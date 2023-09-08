class Account():
    def __init__(self, first_name, last_name, user_name, password):
        self.fname = first_name
        self.lname = last_name
        self.uname = user_name
        self.passwd = password

    def create_new_account(self, user_name, password):
        print('Your username is: ', self.fname)
        print('your password is: ', self.passwd)

person = Account()

person.create_new_account('Philballer', 'Beatballer22')
person.create_new_account('Beatballer', '$Beatballer22')
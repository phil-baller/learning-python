"""class Person:

    TITLES = ('Mr', 'Mrs', 'Ms', 'Dr')

    def __init__(self, title, name, surname):
        self.title = title
        self.name = name
        self.surname = surname
        if title not in self.TITLES:
            print('%s a valid name' % title)

person_title = input('Enter user title: ')
person_first_name = input('Enter user firstname: ')
person_surname = input('Enter user surname: ')

pos = Person(
    person_title,
    person_first_name,
    person_surname
)

pos1 = Person(
    person_title,
    person_first_name,
    person_surname
)

print(pos.title, pos.name, pos.surname)
print(pos1.title, pos1.name, pos1.surname)"""

class Pets:
    def __init__(self):
        self.all_pets = []

    def add_pet(self, pet):
        self.all_pets.append(pet)

    def delete_pet(self):
        self.all_pets.pop()

bob = Pets()
joe = Pets()

while True:
    user_pet = input('Bob and Joe have pets, who do you want to give your pets to: ')
    if user_pet == 'done':
        break
    elif user_pet != 'Bob' and user_pet != 'Joe':
        print('Please select from Bob or Joe')
    if user_pet == 'Bob':
        try:
            while True:
                try:
                    data_pets = input('Enter an animal for Bob: ')
                    bob.add_pet(data_pets)
                    if data_pets == 'done':
                        break
                except TypeError:
                    print('Please enter characters only')
        except:
            print('Error, Enter characters only')
    elif user_pet == 'Joe':
        try:
            while True:
                try:
                    data_pets = input('Enter an animal for Joe: ')
                    joe.add_pet(data_pets)
                    if data_pets == 'done':
                        break
                except TypeError:
                    print('Enter characters only')
        except:
            print('Error, Enter a valid pet')

print(bob.all_pets)
print(joe.all_pets)


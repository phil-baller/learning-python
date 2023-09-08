class Person:

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
print(pos1.title, pos1.name, pos1.surname)
print(pos1.TITLES)
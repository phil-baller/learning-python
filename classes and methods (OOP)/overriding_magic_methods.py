import datetime
class Person:
    def __init__(self, name, surname, birthdate, address, telephone, email):
        self.name = name
        self.surname = surname
        self.birthdate = birthdate
        self.address = address
        self.telephone = telephone
        self.email = email

    def __str__(self):
        return "%s %s, born %s\nAddress: %s\nTelephone: %s\nEmail: %s" %(self.name, self.surname, self.birthdate, self.address,
                                                                         self.telephone, self.email)

person = Person(
    "jane",
    "Doe",
    datetime.date(1992, 5, 6),
    "Chapelle Obili",
    " 555 765 987",
    "philballer41@gmail.com"
)

print(person)

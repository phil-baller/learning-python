class Person:
    TITLES = ('Mr', 'Mrs', 'Dr', 'Ms')

    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    def full_name(self):
        return ('%s %s' % (self.name, self.surname))

    @classmethod
    def first_letters(cls, startswith):
        return [t for t in cls.TITLES if t.startswith(startswith)]

    @staticmethod
    def last_letter(endswith):
        return [v for v in Person.TITLES if v.endswith(endswith)]

jane = Person('Annah', 'Jane')

print(jane.full_name())

print(jane.first_letters('M'))
print(Person.first_letters('M'))

print(jane.last_letter('s'))
print(Person.last_letter('s'))

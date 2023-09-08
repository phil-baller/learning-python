class Person:
    def __init__(self, name, surname):
        self.name = name
        self.surname = surname

    @property
    def full_name(self):
        return ('%s %s' % (self.name, self.surname))

all_names = Person('Anna', 'Smith')

print(all_names.full_name)
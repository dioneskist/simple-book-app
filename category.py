from abc import ABC, abstractmethod
from addressbookexception import AddressBookException


class Category(ABC):
    type = str()

    def __init__(self, type):
        self.type = type

    @abstractmethod
    def add(self):
        pass

    @abstractmethod
    def print(self):
        return ''

    @abstractmethod
    def __repr__(self):
        return self.type

class Family(Category):
    relationship = str()
    valid_relations = ['parent', 'granparent', 'son/daughter', 'aunt/uncle']

    def __init__(self):
        super().__init__(type='Family')

    def add(self):
        self.select_relationship()

    def print_relationship(self):
        print('\nRelationship:')
        index = 0
        for c in self.valid_relations:
            index += 1
            print('[' + str(index) + ']', c)

    def select_relationship(self):
        self.print_relationship()
        select = str(input('\nType category number: '))
        if select.isdecimal() and 0 < int(select) <= len(self.valid_relations):
            self.relationship = self.valid_relations[(int(select) - 1)]
        else:
            raise AddressBookException('Error: Type is not a number or number out of valid options!')

    def print(self):
        return 'Relation: {}'.format(str(self.relationship))

    def __repr__(self):
        return "Category: {} Relation: {}".format(self.type, self.relationship)


class Friends(Category):
    years = int()

    def __init__(self):
        super().__init__(type='Friends')

    def set_year(self, years):
        self.years = years

    def add(self):
        select = str(input('\nType relationship years: '))
        if select.isdecimal():
            self.years = int(select)
        else:
            raise AddressBookException('Error: Type is not a number!')

    def print(self):
        return 'Relation time: {} years'.format(str(self.years))

    def __repr__(self):
        return "Category: {} Relationship years: {}".format(self.type, self.years)


class Acquaintance(Category):
    known = 'yes'

    def __init__(self):
        super().__init__(type='Acquaintance')

    def set_know(self, known):
        self.known = known

    def add(self):
        pass

    def print(self):
        return 'Acquaintance: {}'.format(str(self.known))

    def __repr__(self):
        return "Category: {} Acquaintance: {}".format(self.type, self.known)

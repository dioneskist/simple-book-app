from tabulate import tabulate

from addressbookexception import AddressBookException
from category import Category, Family, Friends, Acquaintance

categories = [Family(), Friends(), Acquaintance()]


def get_attribute(message, attr, accept_blank=False):
    value = str(input(message.format(attr)))
    # if value is blank and accept is true, then return the value
    if not accept_blank and value == '':
        raise AddressBookException('Blank value is not permitted!')
    return value
    # validate value type (int or str) - TO BE IMPLEMENTED


def print_categories():
    print('\nCategories:')
    index = 0
    for c in categories:
        index += 1
        print('[' + str(index) + ']', c.type)


def select_category():
    print_categories()
    select = str(input('\nType category number: '))
    if select.isdecimal() and 0 < int(select) <= len(categories):
        return categories[(int(select) - 1)]
    else:
        raise AddressBookException('Error: Type is not a number or out of range!')


class Person:
    name = ''
    surname = ''
    phone = 0
    email = ''
    haircolor = None
    age = None
    category = None

    def __init__(self, email=None, phone=None, surname=None, name=None):
        self.name = name
        self.surname = surname
        self.phone = phone
        self.email = email

    def __str__(self):
        return "Surname: {} Name: {} Phone: {} Email: {} Hair Color: {} Age: {} {}".format(
            self.surname, self.name,
            self.phone, self.email,
            self.haircolor, self.age, self.category)

    def __iter__(self):
        return self

    def addPerson(self, args):
        if args.name is not None:
            self.name = args.mame
        else:
            self.name = get_attribute('Type the {}: ', 'name')
        if args.surname is not None:
            self.surname = args.surname
        else:
            self.surname = get_attribute('Type the {}: ', 'surname')
        if args.phone is not None:
            self.phone = args.phone
        else:
            self.phone = get_attribute('Type the {}: ', 'phone')
        if args.email is not None:
            self.email = args.email
        else:
            self.email = get_attribute('Type the {}: ', 'email')
        if args.haircolor:
            self.haircolor = get_attribute('Type the {}: ', 'haircolor')
        if args.age:
            age = get_attribute('Type the {}: ', 'age')
            if age.isdecimal():
                self.age = age
            else:
                raise AddressBookException('Age must be a number!')
        self.category = select_category()
        self.category.add()

    def editPerson(self, args):
        name = get_attribute('Type the new {} (enter to maintain the actual value \'' + self.name + '\'): ', 'name',
                             accept_blank=True)
        if name:
            self.name = name

        surname = get_attribute('Type the new {} (enter to maintain the actual value \'' + self.surname + '\'): ',
                                'surname', accept_blank=True)
        if surname:
            self.surname = surname

        phone = get_attribute('Type the new {} (enter to maintain the actual value \'' + self.phone + '\'): ', 'phone',
                              accept_blank=True)
        if phone:
            self.phone = phone

        email = get_attribute('Type the new {} (enter to maintain the actual value \'' + self.email + '\'): ', 'email',
                              accept_blank=True)
        if email:
            self.email = email

        if args.age:
            age = get_attribute('Type the new {} (enter to maintain the actual value \'' + self.age + '\'): ', 'age',
                                accept_blank=True)
            if age:
                self.age = age

        if args.haircolor:
            haircolor = get_attribute(
                'Type the new {} (enter to maintain the actual value \'' + self.haircolor + '\'): ', 'haircolor',
                accept_blank=True)
            if haircolor:
                self.haircolor = haircolor

        self.category = select_category()
        self.category.add()

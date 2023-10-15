import operator
import os

import jsonpickle

from addressbookexception import AddressBookException


class DB:
    dbfilename = ''
    contacts = []

    def __init__(self, dbfilename):
        try:
            self.dbfilename = dbfilename
            if not os.path.isfile(self.dbfilename):
                with open(self.dbfilename, 'w') as db:
                    db.write('')
            else:
                with open(self.dbfilename, 'r') as db:
                    for line in db.readlines():
                        p = jsonpickle.decode(line)
                        self.contacts.append(p)
        except FileExistsError as e:
            raise AddressBookException('Problems to open database. Contact the administrator!' + e)

    def write_contacts(self):
        self.contacts.sort(key=operator.attrgetter('surname'))
        try:
            with open(self.dbfilename, 'w') as db:
                for c in self.contacts:
                    db.write(jsonpickle.encode(c) + '\n')
        except FileExistsError as e:
            raise AddressBookException('Problems to save database. Contact the administrator!' + e)

    def remove(self, selected):
        if 0 <= selected < len(self.contacts):
            del self.contacts[selected]
            self.write_contacts()
            print('Contact deleted!')
        else:
            raise AddressBookException(
                'Contact number ' + str(selected) + ' does not exits! Use display to get contacts.')

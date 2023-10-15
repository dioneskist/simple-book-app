import argparse
from tabulate import tabulate

from addressbookexception import AddressBookException
from db import DB
from person import Person

table_headers = ["Surname", "Name", "Phone", "Email", "Hair Color", "Age", "Category", ""]


def generate_table(contacts):
    table = []
    for c in contacts:
        table.append([c.surname, c.name, c.phone, c.email, c.haircolor, c.age, c.category.type, c.category.print()])
    return table


def print_contacts(contacts):
    if not contacts:
        raise AddressBookException('Address Book empty!')
    generate_table(contacts)
    print(tabulate(generate_table(contacts), table_headers, tablefmt="simple", showindex="always"))


def main():
    args, parser = parse_args()

    # create database or open if exists
    db = DB(args.db)

    try:
        if args.choice == 'add':
            add_contact(args, db)
        elif args.choice == 'display':
            display_contact(db)
        elif args.choice == 'edit':
            edit_contact(db, args)
        elif args.choice == 'remove':
            remove_contact(db)
        else:
            parser.print_help()
    except AddressBookException as e:
        print(e)


def parse_args():
    parser = argparse.ArgumentParser(description='Address Book App\n by Dione Kist')
    subparsers = parser.add_subparsers(dest='choice', help='sub-command help')
    parser_a = subparsers.add_parser('add', help='add contacts')
    parser_a.add_argument('add', help='Create a new contact in Address Book', action='store_true')
    parser_a.add_argument('-n', '--name', type=str, metavar='name', help='name from contact', )
    parser_a.add_argument('-s', '--surname', type=str, metavar='surname', help='surname from contact')
    parser_a.add_argument('-p', '--phone', type=int, metavar='phone', help='prone from contact')
    parser_a.add_argument('-e', '--email', type=str, metavar='email', help='email from contact')
    parser_a.add_argument('-hc', '--haircolor', action='store_true', help='haircolor from contact')
    parser_a.add_argument('-ag', '--age', action='store_true', help='age from contact')

    parser_b = subparsers.add_parser('edit', help='edit contacts in Address Book')
    parser_b.add_argument('edit', help='Edit existing contact in Address Book', action='store_true')
    parser_b.add_argument('-n', '--name', type=str, metavar='name', help='name from contact')
    parser_b.add_argument('-s', '--surname', type=str, metavar='surname', help='surname from contact')
    parser_b.add_argument('-p', '--phone', type=int, metavar='phone', help='prone from contact')
    parser_b.add_argument('-e', '--email', type=str, metavar='email', help='email from contact')
    parser_b.add_argument('-hc', '--haircolor', action='store_true', help='haircolor from contact')
    parser_b.add_argument('-ag', '--age', action='store_true', help='age from contact')
    parser_c = subparsers.add_parser('display', help='display all contacts in Address Book')
    parser_c.add_argument('display', help='Display all contacts in Address Book', action='store_true')
    parser_d = subparsers.add_parser('remove', help='remove contacts in Address Book')
    parser_d.add_argument('remove', help='Remove existing contact in Address Book',
                          action='store_true')
    parser.add_argument('--db', type=str, help='local database (default=db-file.txt)', default='db-file.txt', )
    args = parser.parse_args()
    return args, parser


def display_contact(db):
    print_contacts(db.contacts)


def edit_contact(db, args):
    print_contacts(db.contacts)
    select = str(input('Type contact number: '))
    if select.isdecimal():
        p = db.contacts[int(select)]
        del db.contacts[int(select)]
        p.editPerson(args)
        print('Edited to ' + str(p))
        db.contacts.append(p)
        db.write_contacts()
    else:
        raise AddressBookException('Error: Type is not a number!')


def remove_contact(db):
    print_contacts(db.contacts)
    select = str(input('Type contact number: '))
    if select.isdecimal():
        db.remove(int(select))
    else:
        raise AddressBookException('Error: Type is not a number!')


def add_contact(args, db):
    print('Adding Person to Address Book:')
    p = Person()
    p.addPerson(args)
    db.contacts.append(p)
    db.write_contacts()
    print(p.name + ' added to Address Book!')


if __name__ == '__main__':
    main()

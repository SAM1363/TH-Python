#!/usr/bin/env python3
from collections import OrderedDict
import datetime
import sys
import os
from peewee import *


db = SqliteDatabase('diary.db')


class Entry(Model):
    content = TextField()
    timestamp = DateTimeField(default=datetime.datetime.now)

    class Meta:
        database = db


def initialize():
    """Create the database and the table if they don't exist."""
    db.connect()
    db.create_tables([Entry], safe=True)


def clear():
    os.system('cls' if os.name == 'nt' else 'clear')
    



def menu_loop():
    """Show the menu"""
    choice = None

    while choice  != 'q':
        clear()
        print("Enter 'q' to quit")
        for key , value in menu.items():
            print('{}) {}'.format(key, value.__doc__))
        choice = input('Action: ').lower().strip()

        if choice in menu:
            clear()
            menu[choice]()



def add_entry():
    """Add an entry."""
    print('Enter you entry. press ctr + d when finished.')
    data = sys.stdin.read().strip()

    if data:
        if input('save Entry? [Y/n] ').lower() != 'n':
            Entry.create(content=data)
            print('Saved successfuly!')
    
    
def view_entries(search_entries=None):
    """View previous entries."""
    entries = Entry.select().order_by(Entry.timestamp.desc())

    if search_entries:
        entries = entries.where(Entry.content.contains(search_entries))

    for each in entries:
        timestamp = each.timestamp.strftime('%A %B %d, %Y %I:%M%p')
        clear()
        print(timestamp)
        print('='*len(timestamp))
        print(each.content)
        print('\n\n' + '='*len(timestamp))
        print('n) next entry')
        print('d) to delete entry')
        print('q to return to the main menu')

        next_action = input('Action: [Nq] ').lower().strip()
        if next_action == 'q':
            break
        elif next_action == 'd':
            delete_entry(each)
    
    
def search_entries():
    """Search the entries """
    view_entries(input('Search query: '))

def delete_entry(entry):
    """Delete an entry."""
    if input('Are you shue? [y/n] ').lower() =='y':
        entry.delete_instance()
        print('Deleted!!')


menu = OrderedDict([
    ('a', add_entry),
    ('v', view_entries),
    ('s', search_entries)
])

if __name__ == '__main__':
    initialize()
    menu_loop()



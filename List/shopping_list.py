shopping_list = []

def show_help():
    print("""
    Enter 'help' for help
    Enter 'show' to show the list
    Enter 'done' to finish the list
    Enter 'remove' to delete item from the list
    """)


def add_to_list(item):
    shopping_list.append(item)
    print('added, your list {} items'.format(len(shopping_list)))


def show_list():
    for each in shopping_list:
        print('Your items is {}'.format(each))


def remove_from_list():
    

show_help()

while True:
    new_item = input('> ')

    if new_item == 'DONE'.lower():
        break
    elif new_item == 'HELP'.lower():
        show_help()
        continue
    elif new_item == 'SHOW'.lower():
        show_list()
        continue
    elif new_item == 'REMOVE'.lower():
        remove_from_list()

    add_to_list(new_item)

show_list()
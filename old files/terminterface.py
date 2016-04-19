#!python3
# terminterface.py -- the terminal interface for the personal assistant.
from . helpers import make_numbered as make_numbered

# consider making the menus into classes. 


shopping_list = ['apples', 'pears']
activity_tracker = {'test1': shopping_list, 'test2': shopping_list}

chore_list = {}
main_menu = {'Activity Tracker': activity_tracker, 'Shopping List': shopping_list,
            'Chore List': chore_list}
menus = main_menu.copy()


def print_menu(active_menu):
    numbered_menu = make_numbered(active_menu)

    for index, (key, value) in numbered_menu:
        print '{0}. {1}'.format(index, key)


def menu_selection(active_menu):
    def get_selection(prompt, active_menu):
        """ Get and error check a value."""
        while True:
            try:
                value = int(input(prompt))
            except ValueError:
                print "Please submit a number."
                continue
            if value > len(active_menu.keys()):
                print "Please submit a valid number."
                continue
            if value < 0:
                print "Please submit a valid number."
                continue
            else:
                break
        return value


    selection = get_selection("Please select an option: ", active_menu)
    numbered_menu = make_numbered(active_menu)

    for number, (key, value) in numbered_menu:
        if number == selection:
            if key in menus.keys():
                active_menu = value
                return active_menu
            else:
                print "else condition was met"









""" When I get back, check if isinstance function, list or dictionary """

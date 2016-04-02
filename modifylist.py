#!python3
# modifylist.py -- Module with functions for list modification.
import shelve

def append_list(file_name, list_name, item):

    with shelve.open(file_name, writeback=True) as file:
        file[list_name].append(item)


def remove_from_list(file_name, list_name, item):

    with shelve.open(file_name) as file:
        file[list_name].remove(item)

def write_list_to_file(file_name, list_name):

    with shelve.open(file_name) as file:
        file[list_name] = []

def print_list(file_name, list_name):

    with shelve.open(file_name) as file:
        print file[list_name].keys()

def check_list_for_item(file_name, list_name, item):

    with shelve.open(file_name) as file:
        active_list = file[list_name]
        if item in active_list:
            return True
        else:
            return False







if '__NAME__' == '__MAIN__':
    modify_file()


"""
Some stuff for later, to format lists for display.


for number, item in enumerate(list, 1):
    print('{0}. {1}'.format(number, item)

additionally, think about values needed to associate with timestamps
start_time
stop_time
day_of_week
date
maybe use a class, or otherwise use a dict for each, each dict having the same keys and values, then keep all of the dicts in a dict

Alternatively, use a class. Class variables can be used to track total time for activities. Instance variables can count individual time."""

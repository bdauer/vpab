#!python3
# helpers.py -- Functions with many applications.

def make_numbered(data_structure):
    """  a dict or list. Return an alphabetized enumerate object
    """
    if isinstance(data_structure, dict):
        ordered_menu = sorted(data_structure.items())
        numbered_menu = list(enumerate(ordered_menu, start=1))
        return numbered_menu
    if isinstance(data_structure, list):
        ordered_menu = sorted(data_structure())
        numbered_menu = list(enumerate(ordered_menu, start=1))
        return numbered_menu

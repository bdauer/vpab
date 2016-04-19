"""
class TrackerInterval(db.Model):
    __tablename__ = 'tracker_intervals'
    id = db.column(db.Integer, primary_key=True)
    start_time = db.Column(db.Datetime)
    duration = db.Column(db.Timedelta)

    def __repr__(self):
        return '<TrackerInterval %r>' % (self.start_time)

class ActionList(db.Model):
    __tablename__ = 'action_lists'
    id = db.column(db.Integer, primary_key=True)



NEWEST IDEAS
Make templates.
Home
Login
menu with options (Track Time, Create New List, Schedule Event, Preferences,
each existing list populates here too.)


use :hover with transition-duration on csv buttons. trust me.

Two types of lists. Item and action item.
item would be e.g. a shopping list
action item would be e.g. errands.
Format actions like functions.   go(shopping). buy(turtle). clean(sink).

use make_numbered(list) to get numbered chore_list.

if number is selected, remove the item with that key.

store separate list of items for each special function
(sending sms, email etc)


shopping list menu must contain functions.
Keep both separate.
There's a shopping_list.
Add the names of the functions from a function list to the list
when printing.


### THIS HERE!!! THIS STEP FIRST
to sort stuff in todo list from functions:
use .sort() tuple (n, list) to prioritize items:
add, remove, clear and main menu
are functions from standard_functs.keys()
that always appear after the shopping/chore list.

"""

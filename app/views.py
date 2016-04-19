from flask import render_template
from app import app
from .forms import LoginForm

@app.route('/')
@app.route('/index')
def index():
    menu = [
                # think about how menus fit here.
                # also think about other data you want to save
                # what's local, and what's in the database.

    ]
    return render_template('index.html',
                            #fill in other keys and values here)
            )
def login():
    form = LoginForm()
    return render_template('login.html',
                            #and here)

)
@app.route('/mainmenu')
def mainmenu():
    menu = {'name': 'Main'}
    contents = [
        {
            'name': 'Time Tracker',
            'template': 'timetracker.html'
        },
        {
            'name': 'Create List',
            'template': 'createlist.html'
        },
        {
            'name': 'Schedule Event',
            'template': 'scheduler.html'
        },
        {
            'name': 'Preferences',
            'template': 'preferences.html'
        },

    ]
    return render_template('mainmenu.html',
                            menu=menu,
                            contents=contents)


"""
Backstory:

The mothership landed on (insert a certain number of days, months, years into the future)
bringing vpab to assist. Welcome
         to your futurEEE. unstick_keYYYYYYYY() */end scrambled message*
"""

#! python2.7
# tracktime.py - A module for tracking time.

# use an automatic incrementing integer in the db to handle id's.

import datetime
from itertools import count

class Activity:
    """Create an instance to categorize and track an activity.

    Attributes:

        start_time (datetime): current time at instance initialization.
        stop_time (datetime): current time when end_instance is called.
        time_range (timedelta): difference between stop_time and start_time.
        activity_type (str): the specific type of activity
            ex: coding, working out, watching tv.
            note: these will be grouped into general categories
                  outside of the class.
    """


    def __init__(self):
        self.start_time = datetime.datetime.now()
        self.activity_type = activity_type

    def end_instance(self):
        self.end_time = datetime.datetime.now()
        self.time_range = end_time - start_time

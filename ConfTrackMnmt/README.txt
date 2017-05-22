===========================
Conference Track Management
===========================

Conference Track management tries to manage multiple tracks in a morning and afternoon session. 
Each session contains multiple talks. 
Morning sessions begin at 9am and must finish by 12 noon,for lunch. 
Afternoon sessions begin at 1pm and must finish in time for the networking event. 
The networking event can start no earlier than 4:00 and no later than 5:00. 
No talk title has numbers in it. 
All talk lengths are either in minutes (not hours) or lightning (5 minutes). 
Presenters will be very punctual; there needs to be no gap between sessions. 
Typical usage often looks like this::

from confschedule import ConfTrackManagement

CONF_DIR='/Users/vishnoiprem/interview/thoughtworks/ConfTrackMnmt/'
##This is directory where you will keep project
"""
Please insert desire input file Project Path here:
This module create instancs of ConfTrackManagement class and print desire Conference Track Management
for sessions
"""
c = ConfTrackManagement(CONF_DIR+'ConfTrackManagement/data/test.txt')
print(c.print_output())

Below is input

Writing Fast Tests Against Enterprise Rails 60min
Overdoing it in Python 45min
Lua for the Masses 30min
Ruby Errors from Mismatched Gem Versions 45min
Common Ruby Errors 45min
Rails for Python Developers lightning
Communicating Over Distance 60min
Accounting-Driven Development 45min
Woah 30min
Sit Down and Write 30min
Pair Programming vs Noise 45min
Rails Magic 60min
Ruby on Rails: Why We Should Move On 60min
Clojure Ate Scala (on my project) 45min
Programming in the Boondocks of Seattle 30min
Ruby vs. Clojure for Back-End Development 30min
Ruby on Rails Legacy App Maintenance 60min
A World Without HackerNews 30min
User Interface CSS in Rails Apps 60min

OUTPUT

Track 1:
09:00AM Lua for the Masses 30min
09:30AM Woah 30min
10:00AM Sit Down and Write 30min
10:30AM Programming in the Boondocks of Seattle 30min
11:00AM Ruby vs. Clojure for Back-End Development 30min
11:30AM A World Without HackerNews 30min
12:00PM Lunch
01:00PM Rails for Python Developers lightning
01:05PM Pair Programming vs Noise 45min
01:50PM Clojure Ate Scala (on my project) 45min
02:35PM Writing Fast Tests Against Enterprise Rails 60min
03:35PM Communicating Over Distance 60min
05:00PM Network Event

Track 2:
09:00AM Overdoing it in Python 45min
09:45AM Ruby Errors from Mismatched Gem Versions 45min
10:30AM Common Ruby Errors 45min
11:15AM Accounting-Driven Development 45min
12:00PM Lunch
01:00PM Rails Magic 60min
02:00PM Ruby on Rails: Why We Should Move On 60min
03:00PM Ruby on Rails Legacy App Maintenance 60min
04:00PM User Interface CSS in Rails Apps 60min
05:00PM Network Event


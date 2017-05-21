===========================
Conference Track Management
===========================

Conference Track management tries to manage multiple tracks in a morning and afternoon session. 
Each session contains multiple talks. 
Morning sessions begin at 9am and must finish by 12 noon,
 for lunch. 
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
c = ConfTrackManagement(CONF_DIR+'ConfTrackManagement/resource/test.txt')
print(c.print_output())

from conftrackmanagement import ConfTrackManagement

CONF_DIR='/Users/vishnoiprem/interview/thoughtworks/ConfTrackMnmt/'

"""
Please use desire input file Project Path here:
/Users/vishnoiprem/interview/thoughtworks/ConfTrackMnmt/

This module create instancs of ConfTrackManagement class and print desire Conference Track Management
for sessions

"""
c = ConfTrackManagement(CONF_DIR+'ConfTrackManagement/data/conf_test.txt')
print(c.print_output())
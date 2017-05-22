import unittest
from confschedule import ConfTrackManagement

CONF_DIR='/Users/vishnoiprem/interview/thoughtworks/ConfTrackMnmt/'
##Please use current Working dir

c = ConfTrackManagement(CONF_DIR+"ConfTrackManagement/data/conf_test.txt")


class TestStringMethods(unittest.TestCase):  
    def test_isEmpty(self):
        c = ConfTrackManagement(CONF_DIR+'ConfTrackManagement/data/conf_test.txt')
        #print(c.talk_list)
        self.assertTrue(not c.talk_list)

    def test_isTime(self):
        c = ConfTrackManagement(CONF_DIR+'ConfTrackManagement/data/conf_test3.txt')
        m=sum([c.totaltime(x) for x in c.morning])
        e=sum([c.totaltime(x) for x in c.evening])
        #print(m,e,c.total_time)      
        self.assertTrue(m+e==c.total_time)

    def test_split(self):
        with self.assertRaises(Exception):
            c = ConfTrackManagement('ConfTrackManagement/data/conf_test2.txt')

if __name__ == '__main__':
    unittest.main()
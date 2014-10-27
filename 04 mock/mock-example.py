#! coding: utf-8
from datetime import datetime
from mock import patch, Mock
#from itertools import permutations
import itertools

def real(name):
    for i in itertools.permutations(xrange(len(name))):
        print i

#real("abcabcabcabc")

with patch('itertools.permutations') as perm_mock:
    perm_mock.return_value = [
        (0, 1, 2, 7, 5, 9, 11, 6, 10, 3, 8, 4),
        (0, 1, 2, 7, 5, 9, 11, 6, 10, 4, 3, 8)
        ]
    real("abcabcabcabc")


mock_file = Mock()
mock_file.name = 'my_filename.doc'
mock_file.__iter__ = Mock(return_value = iter(['строка 1', 'строка 2', 'строка 3']))
stat = mock_file.stat.return_value
stat.size, stat.access_time = 1000, datetime(2012, 1, 1)

for line in mock_file:
    print line
print mock_file
print mock_file.name
print mock_file.name2
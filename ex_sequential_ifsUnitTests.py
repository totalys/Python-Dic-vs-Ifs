import unittest

input01 = [
    'append 1',
    'append 6',
    'append 10',
    'append 8',
    'append 9',
    'append 2',
    'append 12',
    'append 7',
    'append 3',
    'append 5',
    'insert 8 66',
    'insert 1 30',
    'insert 6 75',
    'insert 4 44',
    'insert 9 67',
    'insert 2 44',
    'insert 9 21',
    'insert 8 87',
    'insert 1 75',
    'insert 1 48',
    'print',
    'reverse',
    'print',
    'sort',
    'print',
    'append 2',
    'append 5',
    'remove 2',
    'print'
]

expectedOutput = [
    '[1, 48, 75, 30, 44, 6, 10, 44, 8, 9, 87, 75, 21, 2, 67, 12, 7, 66, 3, 5]',
    '[5, 3, 66, 7, 12, 67, 2, 21, 75, 87, 9, 8, 44, 10, 6, 44, 30, 75, 48, 1]',
    '[1, 2, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87]',
    '[1, 3, 5, 6, 7, 8, 9, 10, 12, 21, 30, 44, 44, 48, 66, 67, 75, 75, 87, 2, 5]'
    ]

class TestPartOne(unittest.TestCase):

    def test_01_resolveListCommands(self):
        self.assertEqual(resolveListCommands(input01), expectedOutput)   

def runTests():
    suite = unittest.defaultTestLoader.loadTestsFromTestCase(TestPartOne)
    unittest.TextTestRunner(verbosity = 2, failfast = True).run(suite)

try:
    from ex_sequential_ifs import *
except:
    pass

from stopWatch import StopWatch
stopWatch = StopWatch()
stopWatch.start()
for n in range(500):
    runTests()
stopWatch.stop()
print(f'Elipsed: {stopWatch.elapsed()}')

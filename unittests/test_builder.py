import os
import sys
import unittest
sys.path.append(os.getcwd())
from machine_builder import *
from models.turing_machine import *

class BuilderTest(unittest.TestCase):
    
    def test_build(self):
        machine = TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']],)
        builded1 = machine_builder(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']])
        builded2 = machine_builder(['aaba', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']])
        builded3 = machine_builder(['aaaa', 'v', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']])
        builded4 = machine_builder(['aaba', 'a', 'aaasaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']])
        builded5 = machine_builder(['aaba', 'a', 'aaaaa'],
                                    {0, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']])
        builded6 = machine_builder(['aaba', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7, 15}, {15}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']])
        builded7 = machine_builder(['aaba', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0, None,
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Left']])
        builded8 = TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0,' None',
                                    [[0, 'a', '_', 'v', 1, 'Right'],
                                    [0, 'b', '_', 'v', 2, 'Right']],)

        self.assertEqual(machine, builded1)
        self.assertNotEqual(machine, builded2)
        self.assertNotEqual(machine, builded3)
        self.assertNotEqual(machine, builded4)
        self.assertNotEqual(machine, builded5)
        self.assertNotEqual(machine, builded6)
        self.assertNotEqual(machine, builded7)
        self.assertNotEqual(machine, builded8)


if __name__ == '__main__':
    unittest.main()

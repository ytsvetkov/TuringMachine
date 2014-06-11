import sys
import unittest
sys.path.append('/home/thepuppeteer/Projects/Python/Project/')
from turing_machine import *
from rule import *


class MachineTest(unittest.TestCase):
    
    def test_correct_states(self):
        self.assertTrue(isinstance(TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],), TuringMachine))
        with self.assertRaises(StateError):
            TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {5}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],)
        with self.assertRaises(StateError):
            TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {15}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],)
        with self.assertRaises(StateError):
            TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 7}, {5}, {6}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],)
        with self.assertRaises(StateError):
            TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {5}, 10,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],)

    def test_equality(self):
        machine1 = TuringMachine(['aaaaaa', 'a', 'aaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],)
        machine2 = TuringMachine(['aaaa', 'a', 'aaaaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [0, 'b', '_', 2, 'Right']],)
        machine2.tape.move_head_right()
        machine2.tape.move_head_right()
        self.assertTrue(machine1, machine2)

    def test_step(self):
        machine1 = TuringMachine(['aaaaaa', 'a', 'aaa'],
                                    {0, 1, 2, 3, 4, 5, 6, 7}, {5}, {6}, 0,
                                    [[0, 'a', '_', 1, 'Right'],
                                    [1, 'a', 'c', 3, 'Right']],)
        self.assertTrue(machine1.step(), Rule(*[0,'a','_',1,'Right']))
        self.assertTrue(machine1.step(), Rule(*[1,'a','c',3,'Right']))

if __name__ == '__main__':
    unittest.main()

import sys
import unittest
sys.path.append('/home/thepuppeteer/Projects/Python/Project/')
from input_parser import *


class InputParserTest(unittest.TestCase):

    def test_tape_parsing(self):
        test_tape = parse_tape_from_terminal('(sdhfsdil,s,sadijsal)')
        correct_tape = ["sdhfsdil", 's', "sadijsal"]
        self.assertEqual(test_tape, correct_tape)

        test_tape2 = parse_tape_from_terminal(
            '   ( 01 10 101 0 10 ,5, 4   4 86 4)  ')
        correct_tape2 = [' 01 10 101 0 10 ', '5', ' 4   4 86 4']
        self.assertEqual(test_tape2, correct_tape2)

    def tttttest_states_parsing(self):
        test_states = {1,2,3}
        parsed_states = parse_states_from_terminal('1, 2, 3')
        self.assertEqual(test_states, parsed_states)

    def test_initial_state_parse(self):
        self.assertEqual(1, parse_initial_from_terminal('1'))
        self.assertEqual(123, parse_initial_from_terminal('123'))
        self.assertNotEqual(1212, parse_initial_from_terminal('1212  '))
        self.assertNotEqual(1321, parse_initial_from_terminal('1212'))
        self.assertNotEqual(1212, parse_initial_from_terminal('213'))
        self.assertNotEqual(1212, parse_initial_from_terminal('1 21 2'))

    def test_rules(self):
        self.assertEqual([1,'a','a',1,'None'], parse_rule_from_terminal('(1,a,a,1,None)'))
        self.assertEqual([1,'a','b',2,'Left'], parse_rule_from_terminal('(1,a,b,2,Left)'))
        self.assertEqual([1,'a','a',1,'Right'], parse_rule_from_terminal('(1,a,a,1,Right)'))
        self.assertNotEqual([2,'a','a',1,'Right'], parse_rule_from_terminal('(1,a,a,1,Right)'))
        self.assertNotEqual([1,'b','a',1,'Right'], parse_rule_from_terminal('(1,a,a,1,Right)'))
        self.assertNotEqual([1,'a','v',1,'Right'], parse_rule_from_terminal('(1,a,a,1,Right)'))
        self.assertNotEqual([1,'a','a',3,'Right'], parse_rule_from_terminal('(1,a,a,1,Right)'))
        self.assertNotEqual([1,'a','a',1,'Left'], parse_rule_from_terminal('(1,a,a,1,Right)'))

if __name__ == '__main__':
    unittest.main()

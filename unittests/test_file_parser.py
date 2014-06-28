import os
import sys
import unittest
sys.path.append(os.getcwd())
from parsing.file_parser import *


class FileParserTest(unittest.TestCase):
    
    def test_parse_tape(self):
        self.assertEqual(parse_tape_from_file('tape: (asd,a,asd)', 0), ['asd', 'a', 'asd'])
        self.assertEqual(parse_tape_from_file('tape: (,a,asd)', 0), ['', 'a', 'asd'])
        self.assertEqual(parse_tape_from_file('tape: (,,)', 0), ['', '', ''])
        self.assertEqual(parse_tape_from_file('tape: (asd,a,)', 0), ['asd', 'a', ''])
        self.assertEqual(parse_tape_from_file('tape: (ada#dsd,a,afdas)d)', 0), ['ada#dsd', 'a', 'afdas)d'])

        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('tpe: (asd,a,asd)', 0), '')
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('tape: (asda,asd)', 0), '')
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('tape: (asdaasd)', 0), '')
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('tape: (asd,a,asd', 0), '')
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('tape: asd,a,asd)', 0), '')
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('tape (asd,a,asd)', 0), '')
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_tape_from_file('(tape asd,a,asd)', 0), '')

    def test_parse_states(self):
        self.assertEqual(parse_states_from_file('states: {1,2,3,4,5}', 0),
            set([1, 2, 3,4,5]))
        self.assertEqual(parse_states_from_file('states: {1}', 0), set([1]))
        self.assertEqual(parse_states_from_file('states: {}', 0), set())

        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_states_from_file('stes: {}', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_states_from_file('states {}', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_states_from_file('states: {1,2,3', 0), 0)


    def test_parse_initial(self):
        self.assertEqual(parse_initial_from_file('initial: 0', 0), 0)
        self.assertEqual(parse_initial_from_file('initial: 123', 0), 123)
        self.assertEqual(parse_initial_from_file('initial: 10', 0), 10)
        self.assertEqual(parse_initial_from_file('initial: 00', 0), 0)

        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_initial_from_file('initial 0', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_initial_from_file('inial: 0', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_initial_from_file('inial:', 0), 0)

    def test_parse_rule(self):
        self.assertEqual(parse_rule_from_file('(0,b,a,b,0,Right)', 0),
            [0, 'b', 'a', 'b', 0, 'Right'])
        self.assertEqual(parse_rule_from_file('(0,_,_,_,1,None)', 0),
            [0, '_', '_', '_', 1, 'None'])
        self.assertEqual(parse_rule_from_file('(0,_,_,_,1,Left)', 0),
            [0, '_', '_', '_', 1, 'Left'])

        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_rule_from_file('(0,_,_,_,1,No)', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_rule_from_file('(0,_,_,_,None)', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_rule_from_file('(a,_,_,_,1,None)', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_rule_from_file('(0,_,_,_,b,None)', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_rule_from_file('(0,_,_,_,1,None', 0), 0)

    def test_parse_accept_states(self):
        self.assertEqual(parse_accept_states_from_file('accept: {1}', 0),
            set([1]))
        self.assertEqual(parse_accept_states_from_file('accept: {1}', 0), set([1]))
        self.assertEqual(parse_accept_states_from_file('accept: {}', 0), set())

        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_accept_states_from_file('acce: {}', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_accept_states_from_file('accept {}', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_accept_states_from_file('accept: {1,2,3', 0), 0)

    def test_parse_reject_states(self):
        self.assertEqual(parse_reject_states_from_file('reject: {1}', 0),
            set([1]))
        self.assertEqual(parse_reject_states_from_file('reject: {1}', 0), set([1]))
        self.assertEqual(parse_reject_states_from_file('reject: {}', 0), set())

        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_reject_states_from_file('acce: {}', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_reject_states_from_file('reject {}', 0), 0)
        with self.assertRaises(SyntacticError):
            self.assertEqual(parse_reject_states_from_file('reject: {1,2,3', 0), 0)

if __name__ == '__main__':
    unittest.main()

import sys
import unittest
sys.path.append('/home/thepuppeteer/Projects/Python/Project/')
from input_parser import *


class InputParserTest(unittest.TestCase):
    def test_tape_parsing(self):
        test_tape = parse_tape_from_terminal('(sdhfsdil,s,sadijsal)')
        correct_tape = ["sdhfsdil",'s',"sadijsal"]
        self.assertEqual(test_tape, correct_tape)

        test_tape2 = parse_tape_from_terminal('   ( 01 10 101 0 10 ,5, 4   4 86 4)  ') 
        correct_tape2 = [' 01 10 101 0 10 ','5',' 4   4 86 4']
        self.assertEqual(test_tape2, correct_tape2)

if __name__ == '__main__':
    unittest.main()

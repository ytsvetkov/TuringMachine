import os
import sys
import unittest
sys.path.append(os.getcwd())
from models import rule_book



class RulesTest(unittest.TestCase):

    def test_deterministic(self):
        rule1 = [1, 'a', 'a', 'v',1, 'Left']
        rule2 = [1, 'a', 'b', 'v',2, 'Right']
        self.assertRaises(TypeError, rule_book.Rule_Book, rule1, rule2)

        rule3 = [1, 'b', 'a', 'v',1, 'Right']
        rules = rule_book.Rule_Book([rule1, rule3])
        self.assertTrue(rules.is_deterministic())


if __name__ == '__main__':
    unittest.main()

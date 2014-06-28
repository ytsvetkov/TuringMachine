import os
import sys
import unittest
sys.path.append(os.getcwd())
from models import rule_book, rule



class RulesTest(unittest.TestCase):

    def test_deterministic(self):
        rule1 = [1, 'a', 'a', 'v',1, 'Left']
        rule2 = [1, 'a', 'b', 'v',2, 'Right']
        self.assertRaises(TypeError, rule_book.Rule_Book, rule1, rule2)

        rule3 = [1, 'b', 'a', 'v',1, 'Right']
        rules = rule_book.Rule_Book([rule1, rule3])
        self.assertTrue(rules.is_deterministic())

        rule5 = [1, 'a', 'д', 'v',1, 'None']
        rule6 = [1, 'a', 'b', 'е',2, 'None']
        self.assertRaises(TypeError, rule_book.Rule_Book, rule5, rule6)

    def test_apply(self):
        rule1 = [1, 'a', 'a', 'v',1, 'Left']
        rule2 = [2, 'b', 'a', 'v',1, 'Right']
        rule3 = [3, 'c', 'a', 'v',1, 'Left']
        book = rule_book.Rule_Book([rule1, rule2, rule3])
        self.assertTrue(book.can_be_applied(1, 'a'))
        self.assertTrue(book.can_be_applied(2, 'b'))
        self.assertTrue(book.can_be_applied(3, 'c'))
        self.assertFalse(book.can_be_applied(21, 'a'))
        self.assertFalse(book.can_be_applied(31, 'v'))
        self.assertFalse(book.can_be_applied(3, 'l'))

    def test_get_rule(self):
        rule1 = [1, 'a', 'a', 'v',1, 'Left']
        rule2 = [2, 'b', 'a', 'v',1, 'Right']
        rule3 = [3, 'c', 'a', 'v',1, 'Left']
        book = rule_book.Rule_Book([rule1, rule2, rule3])
        self.assertEqual(book.get_rule(1,'a'), rule.Rule(*rule1))
        self.assertEqual(book.get_rule(2,'b'), rule.Rule(*rule2))
        self.assertEqual(book.get_rule(3,'c'), rule.Rule(*rule3))
        self.assertEqual(book.get_rule(1,'b'), None)
        self.assertEqual(book.get_rule(22,'v'), None)
        self.assertEqual(book.get_rule(33,'c'), None)


if __name__ == '__main__':
    unittest.main()

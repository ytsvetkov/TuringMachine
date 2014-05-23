import unittest
import rule
import rule_book

class RulesTest(unittest.TestCase):

    def test_deterministic(self):
        rule1 = rule.Rule(1, 'a', 'a', 1, 'Left')
        rule2 = rule.Rule(1, 'a', 'b', 2, 'Right')
        self.assertRaises(TypeError, rule_book.Rule_Book, rule1, rule2)

        rule3 = rule.Rule(1, 'b', 'a', 1, 'Right')
        rules = rule_book.Rule_Book(rule1, rule3)
        self.assertTrue(rules.is_deterministic())


if __name__ == '__main__':
    unittest.main()

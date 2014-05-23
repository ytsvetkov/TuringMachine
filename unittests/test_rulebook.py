import unittest
import rule
import rule_book

class RulesTest(unittest.TestCase):

    def test_deterministic(self):
        rule1 = rule.Rule(1, 'a', 'a', 1, 'Left')
        rule2 = rule.Rule(1, 'a', 'b', 2, 'Right')
        rules = rule_book.Rule_Book(rule1, rule2)
        self.assertFalse(rules.is_deterministic())


if __name__ == '__main__':
    unittest.main()

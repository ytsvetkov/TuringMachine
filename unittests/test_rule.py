import sys
import unittest
sys.path.append('/home/thepuppeteer/Projects/Python/Project/')
from rule import Rule


class RuleTest(unittest.TestCase):
    
    def test_can_be_applied(self):
        rule = Rule(1,'a', 'b', 2, 'Left')
        self.assertTrue(rule.can_be_applied(1,'a'))
        self.assertFalse(rule.can_be_applied(2,'a'))
        self.assertFalse(rule.can_be_applied(1,'b'))

    def test_equality(self):
        rule1 = Rule(1,'a', 'f', 2, 'None')
        rule2 = Rule(1,'a', 'f', 2, 'None')
        rule3 = Rule(1,'a', 'f', 3, 'None')
        rule4 = Rule(2,'a', 'f', 3, 'None')
        rule5 = Rule(2,'2', 'f', 3, 'None')
        rule6 = Rule(2,'2', 'w', 3, 'None')
        rule7 = Rule(2,'2', 'w', 3, 'Left')
        rule8 = Rule(22,'A', 'C', 23, 'Right')

        self.assertTrue(rule1 == rule1)
        self.assertTrue(rule1 == rule2)
        self.assertFalse(rule1 == rule3)
        self.assertFalse(rule1 == rule4)
        self.assertFalse(rule1 == rule5)
        self.assertFalse(rule1 == rule6)
        self.assertFalse(rule1 == rule7)
        self.assertFalse(rule1 == rule8)
        self.assertFalse(rule7 == rule1)

if __name__ == '__main__':
    unittest.main()

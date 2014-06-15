import os
import sys
sys.path.append(os.getcwd())
from models import rule as _rule


class Rule_Book:

    def __init__(self, rules):
        self.rules = []
        for rule in rules:
            self.rules.append(_rule.Rule(*rule))
        self.is_deterministic()

    def __repr__(self):
        string = ''
        for i in self.rules:
            string += str(i) + '\n'
        return string

    def __eq__(self, other):
        for i in self.rules:
            if i not in other.rules:
                return False
        return len(self.rules) == len(other. rules)

    def __getitem__(self, index):
        return self.rules[index]

    def __len__(self):
        return len(self.rules)

    def is_deterministic(self):
        for rule_1 in self.rules:
            for rule_2 in self.rules:
                if (rule_1 != rule_2) and\
                    (rule_1.read_character == rule_2.read_character) and\
                        (rule_1.current_state == rule_2.current_state):
                    raise TypeError("This allows nondeterministic behaviour!")
        return True

    def add_rule(self, rule):
        self.rules.append(rule)
        self.is_deterministic

    def can_be_applied(self, read_character, state):
        for rule in self.rules:
            if rule.can_be_applied(read_character, state):
                return True
        return False

    def get_rule(self, state, character):
        for rule in self.rules:
            if rule.can_be_applied(state, character):
                return rule

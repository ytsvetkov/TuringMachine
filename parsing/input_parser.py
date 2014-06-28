import sys
import re


class SyntacticError(Exception):

    def __init__(self, message):
        self.message = message


user_tape_regex = r'^\s*\(.*,.,.*\)\s*$'
user_states_regex = r'^([0-9]*,)*[0-9]+$'
user_initial_regex = r'^[0-9]+$'
user_rule_regex = r'^\([0-9]{1,},.,.,.,[0-9]{1,},(Left|None|Right)\)$'


def parse_tape_from_terminal(input_tape):
    tape = re.match(user_tape_regex, input_tape.strip('\n '))
    if tape is None:
        raise SyntacticError('There is syntactic error with this tape !')
    else:
        return tape.group().strip(')(').split(',')


def parse_states_from_terminal(input_states):
    states = re.match(user_states_regex, input_states.strip('\n'))
    if states is None:
        raise SyntacticError('There is syntactic error with these states !')
    else:
        machine_states = set()
        for state in states.group().strip('}').split(','):
            machine_states.add(int(state))
        return machine_states


def parse_initial_from_terminal(input_initial_state):
    initial = re.match(user_initial_regex, input_initial_state.strip('\n'))
    if initial is None:
        raise SyntacticError('There is syntactic error with the'
                             'initial state !')
    else:
        return int(initial.group())


def parse_rule_from_terminal(input_rule):
    input_rule = re.match(user_rule_regex, input_rule)
    if input_rule is None:
        raise SyntacticError('There is syntactic error with this rule !')
    else:
        rule = input_rule.group().strip('\n)(').split(',')
        rule[0] = int(rule[0])
        rule[4] = int(rule[4])
    return rule

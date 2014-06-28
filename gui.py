import sys
import os
import re
from parsing import file_parser
from parsing import input_parser
import machine_builder
from visualisation import animation


tape = ''
states = set()
reject_states = set()
accept_states = set()
initial_state = 0
rules = []


structures = {0: (
    'Initialise the tape\n', input_parser.parse_tape_from_terminal),
    1: ('Enter the states:\n', input_parser.parse_states_from_terminal),
    2: ('Enter the accept states\n', input_parser.parse_states_from_terminal),
    3: ('Enter the reject states\n', input_parser.parse_states_from_terminal),
    4: ('Enter the initial state\n', input_parser.parse_initial_from_terminal),
    5: ('Enter rule\n', input_parser.parse_rule_from_terminal)
}

machine_parts = {0: tape,
                 1: states,
                 2: accept_states,
                 3: reject_states,
                 4: initial_state
                 }


def user_input(i, struct=None):
    while True:
        struct = input(structures[i][0])
        struct = structures[i][1](struct)
        if isinstance(struct, input_parser.SyntacticError):
            print(struct.message)
        else:
            return struct

def user_rule(i, struct=None):
    try:
        rule = input('Enter a rule\n')
        rule = input_parser.parse_rule_from_terminal(rule)
        rules.append(rule)
    except input_parser.SyntacticError as err:
        print(err.message)

def main_cli_action():

    for i in range(5):
        while True:
            try:
                machine_parts[i] = user_input(i, structures[i][1])
                break
            except input_parser.SyntacticError as err:
                print(err.message)

    stack = input('Enter the initial stack\n')

    try:
        while True:
            user_rule(5, structures[5][1])
    except EOFError:
        return machine_builder.machine_builder(
            machine_parts[0], machine_parts[1], machine_parts[2],
            machine_parts[3], machine_parts[4], stack, rules)
    except input_parser.SyntacticError as err:
        print(err)
try:
    machine = file_parser.parse_validator_from_file(sys.argv[1])
    machine = machine_builder.machine_builder(*machine)
    animation.Animate(machine)
except ZeroDivisionError:
    pass
except (input_parser.SyntacticError, file_parser.SyntacticError):
    pass
except IndexError:
    machine = main_cli_action()
    animation.Animate(machine)
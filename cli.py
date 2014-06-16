import sys
import os
import re
from parsing import file_parser
from parsing import input_parser
import machine_builder
from visualisation import automata_graph


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
    4: ('Enter the initial state\n', input_parser.parse_initial_from_terminal)
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


def main_cli_action():

    for i in range(5):
        machine_parts[i] = user_input(i, structures[i][1])
    stack = input('Enter the initial stack\n')

    try:
        while True:
            rule = input('Enter a rule\n')
            rule = input_parser.parse_rule_from_terminal(rule)
            if isinstance(rule, input_parser.SyntacticError):
                print(rule.message)
            else:
                rules.append(rule)
    except EOFError:
        return machine_builder.machine_builder(
            machine_parts[0], machine_parts[1], machine_parts[2],
            machine_parts[3], machine_parts[4], stack, rules)

try:
    machine = file_parser.parse_validator_from_file(sys.argv[1])
    try:
        print(machine_builder.machine_builder(*machine).run())
    except TypeError as err:
        print("Error with the machine !!!")
        print(err)
    draw_automata_decision = input(
        "Do you want to see a graphical representation ?\n")
    if draw_automata_decision == 'y' or draw_automata_decision == 'yes':
        automata_graph.draw_automata(machine_builder.machine_builder(*machine))
except IndexError:
    machine = main_cli_action()
    print(machine.run())
    draw_automata_decision = input(
        "Do you want to see a graphical representation ?\n")
    if draw_automata_decision == 'y' or draw_automata_decision == 'yes':
        automata_graph.draw_automata(machine)

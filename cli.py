import sys
import os
import re
import file_parser
import input_parser
from turing_machine import *


accept_invite_message = 'If you need another accept state, enter the number !\n'
reject_invite_message = 'If you need another reject state, enter the number !\n'
unaccepted_value_message = 'Unacceptable value for accept state. Please enter again !\n'
current_message = 'If you need accept state, enter the number !\n'

states = set()
reject_states = set()
accept_states = set()
rules = []


def main_cli_action():

    tape = input('Initialise the tape:\n')
    states = input('Enter the states:\n')
    accept_states = input('Enter the accept states\n')
    reject_states = input('Enter the reject states\n')
    initial_state = input('Enter the initial state\n')
    print(('Enter a rule or press Ctrl+D for end of rules'))
    try:
        while True:
            rule = input()
            rules.append(rule)
    except EOFError:
        return input_parser.parse_validator_from_terminal(rules, states, accept_states,
                                             reject_states, initial_state, tape)


try:
    sys.argv[1]
    machine = file_parser.parse_validator_from_file(sys.argv[1])
    print(machine.run())
except:
    machine = main_cli_action()
    print(machine.run())
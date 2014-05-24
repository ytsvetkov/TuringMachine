import sys
import os
import re
import file_parser
import input_parser
from turing_machine import *
import machine_builder


accept_invite_message = 'If you need another accept state, \
                        enter the number !\n'
reject_invite_message = 'If you need another reject state, \
                        enter the number !\n'
unaccepted_value_message = 'Unacceptable value for accept state. \
                        Please enter again !\n'
current_message = 'If you need accept state, enter the number !\n'

states = set()
reject_states = set()
accept_states = set()
rules = []


def main_cli_action():

    while True:
        tape = input('Initialise the tape:\n')
        tape = input_parser.parse_tape_from_terminal(tape)
        if isinstance(tape, input_parser.SyntacticError): print('error')
        else: break

    while True:
        states = input('Enter the states:\n')
        states = input_parser.parse_states_from_terminal(states)
        if isinstance(states, input_parser.SyntacticError): print('error')
        else: break
        
    while True:
        accept_states = input('Enter the accept states\n')
        accept_states = input_parser.parse_states_from_terminal(accept_states)
        if isinstance(accept_states, input_parser.SyntacticError): print('error')
        else: break

    while True:
        reject_states = input('Enter the reject states\n')
        reject_states = input_parser.parse_states_from_terminal(reject_states)
        if isinstance(reject_states, input_parser.SyntacticError): print('error')
        else: break

    while True:
        initial_state = input('Enter the initial state\n')
        initial_state = input_parser.parse_initial_from_terminal(initial_state)
        if isinstance(initial_state, input_parser.SyntacticError): print('error')
        else: break

    try:
        while True:
            rule = input('Enter a rule\n')
            rule = input_parser.parse_rule_from_terminal(rule)
            if isinstance(rule, input_parser.SyntacticError): print('error')
            else: rules.append(rule)
    except EOFError:
        return machine_builder.machine_builder(tape, states, accept_states,
                    reject_states, initial_state, rules)


try:
    sys.argv[1]
    machine = file_parser.parse_validator_from_file(sys.argv[1])
    print(machine.run())
except:
    machine = main_cli_action()
    print(machine.run())

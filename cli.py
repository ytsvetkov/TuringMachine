import sys
import os
import re
import parser
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

    # states = input('Please enter the number of states you are going to use !\n')
    # states = int(states)


    # try:
    #     while True:
    #         accept_state = input(current_message)
    #         accept_state = int(accept_state)
    #         if (0 <= accept_state < states) and (accept_state not in accept_states):
    #             accept_states.add(accept_state)
    #             current_message = accept_invite_message
    #         else:
    #             current_message = unaccepted_value_message
    # except:
    #     current_message = 'If you need reject state, enter the number !\n'


    # try:
    #     while True:
    #         reject_state = input(current_message)
    #         reject_state = int(reject_state)
    #         if (0 <= reject_state < states) and (reject_state not in reject_states)\
    #                 and (reject_state not in accept_states):
    #             reject_states.add(reject_state)
    #             current_message = reject_invite_message
    #         else:
    #             current_message = unaccepted_value_message
    # except:
    #     print('exit')




    # tape = input('Initialise the tape:\n')
    # parser.parse_validator_from_terminal(1,2,3,4,5,tape)
    # states = input('Enter the states:\n')
    # parser.parse_validator_from_terminal(1,states,3,4,5,6)
    # accept_states = input('Enter the accept states\n')
    # parser.parse_validator_from_terminal(1,2,accept_states,4,5,6)
    # reject_states = input('Enter the reject states\n')
    # parser.parse_validator_from_terminal(1,2,3,reject_states,5,6)
    # initial_state = input('Enter the initial state\n')
    # parser.parse_validator_from_terminal(1,2,3,4,initial_state,6)
    print(('Enter a rule or press Ctrl+D for end of rules'))
    try:
        while True:
            x = input()
            rules.append(x)
    except EOFError: 
        parser.parse_validator_from_terminal(rules,2,3,4,5,6)



# try:
#     sys.argv[1]
#     machine = parser.parse_validator(sys.argv[1])
#     print(machine.run())
# except:
main_cli_action()

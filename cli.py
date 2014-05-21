import sys
import os
import re


accept_invite_message = 'If you need another accept state, enter the number !\n'
reject_invite_message = 'If you need another reject state, enter the number !\n'
unaccepted_value_message = 'Unacceptable value for accpet state. Please enter again !\n'
current_message = 'If you need accept state, enter the number !\n'


reject_states = set()
accept_states = set()



def main_cli_action():

    states = input('Please enter the number of states you are going to use !\n')
    states = int(states)


    try:
        while True:
            accept_state = input(current_message)
            accept_state = int(accept_state)
            if (0 <= accept_state < states) and (accept_state not in accept_states):
                accept_states.add(accept_state)
                current_message = accept_invite_message
            else:
                current_message = unaccepted_value_message
    except:
        current_message = 'If you need reject state, enter the number !\n'


    try:
        while True:
            reject_state = input(current_message)
            reject_state = int(reject_state)
            if (0 <= reject_state < states) and (reject_state not in reject_states)\
                    and (reject_state not in accept_states):
                reject_states.add(reject_state)
                current_message = reject_invite_message
            else:
                current_message = unaccepted_value_message
    except:
        print('exit')


# try:
#     sys.argv[1]
#     while True:
#         program = open(sys.argv[1], 'r'):
#         x=program.readline()
#         print(x)
# except:
#     main_cli_action()

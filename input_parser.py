import sys
import re
import machine_builder


class SyntacticError(Exception):

    def __init__(self, message, messed_line):
        self.message = message
        self.messed_line = messed_line


machine_rules = []
states = set()
accept_states = set()
reject_states = set()


user_tape_regex = r'^\s*\(.*,.,.*\)$'
user_states_regex = r'^([0-9]*,)*[0-9]+$'
user_initial_regex = r'^[0-9]+$'
user_rule_regex = r'^\([0-9]{1,},.,.,[0-9]{1,},(Left|None|Right)\)$'


def parse_validator_from_terminal(ruless, statess, accept_statess,
                                  reject_statess, initial_statee, tapee):
    if re.match(user_tape_regex, tapee.strip('\n')) == None:
        print('error')
    else:
        turing_tape = re.match(user_tape_regex, tapee.strip('\n'))
        initial_tape = turing_tape.group().strip(')(').split(',')

    if re.match(user_states_regex, statess.strip('\n')) == None:
        print('error')
    else:
        turing_states = re.match(user_states_regex, statess.strip('\n'))
        for state in turing_states.group().strip('}').split(','):
            states.add(int(state))

    if accept_statess == '':
        print('accept: ', accept_states)
    elif re.match(user_states_regex, accept_statess.strip('\n')) == None:
        print('error')
    else:
            turing_accept = re.match(
                user_states_regex, accept_statess.strip('\n'))
            for state in turing_accept.group().strip('}').split(','):
                accept_states.add(int(state))

    if reject_statess == '':
        print('reject: ', reject_states)
    elif re.match(user_states_regex, reject_statess.strip('\n')) == None:
        print('error')
    else:
            turing_accept = re.match(
                user_states_regex, reject_statess.strip('\n'))
            for state in turing_accept.group().strip('}').split(','):
                reject_states.add(int(state))

    if re.match(user_initial_regex, initial_statee.strip('\n')) == None:
        print('error')
    else:
            turing_initial = re.match(
                user_initial_regex, initial_statee.strip('\n'))
            initial_state = int(turing_initial.group())

    for rulee in ruless:
        if re.match(user_rule_regex, rulee) == None:
            raise SyntacticError(rulee, 434)
        else:
            turing_rule = rulee.strip('\n)(').split(',')
            turing_rule[0] = int(turing_rule[0])
            turing_rule[3] = int(turing_rule[3])
            machine_rules.append(turing_rule)

    return machine_builder.machine_builder(initial_tape, states, accept_states,
                                           reject_states, initial_state,
                                           machine_rules)

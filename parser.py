import sys
import re
import rule
import tape
from turing_machine import *


class SyntacticError(Exception):

    def __init__(self, message, messed_line):
        self.message = message
        self.messed_line = messed_line


machine_rules = []
states = set()
accept_states = set()
reject_states = set()
initial_tape = tape.Tape('','','')


rule_regex = r'^\([0-9]{1,},.,.,[0-9]{1,},(Left|None|Right)\)$'
states_regex = r'^(states:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
accept_regex = r'^(accept:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
reject_regex = r'^(reject:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
initial_regex = r'^(initial:\s*)([0-9]*)$'
tape_regex = r'^(tape:\s*)(\((.)*,(.)*,(.)*\))$'


def parse_validator(program_name = None):
    line_counter = 1
    try:
        with open(program_name, "rt") as program:
            for line in program:
                if line == '\n':
                    line_counter += 1
                elif re.match(rule_regex, line.strip('\n')):
                    turing_rule = line.strip('\n)(').split(',')
                    turing_rule[0] = int(turing_rule[0])
                    turing_rule[3] = int(turing_rule[3])
                    machine_rules.append(rule.Rule(*turing_rule))
                    line_counter += 1
                elif re.match(states_regex, line.strip('\n')) != None:
                    turing_states = re.match(states_regex, line.strip('\n'))
                    for state in turing_states.group(2).strip('}').split(','):
                        states.add(int(state))
                    line_counter += 1
                elif re.match(accept_regex, line.strip('\n')) != None:
                    turing_accept = re.match(accept_regex, line.strip('\n'))
                    for state in turing_accept.group(2).strip('}').split(','):
                        accept_states.add(int(state))
                    line_counter += 1
                elif re.match(reject_regex, line.strip('\n')) != None:
                    turing_reject = re.match(reject_regex, line.strip('\n'))
                    for state in turing_reject.group(2).strip('}').split(','):
                        reject_states.add(int(state))
                    line_counter += 1
                elif re.match(tape_regex, line.strip('\n')) != None:
                    turing_tape = re.match(tape_regex, line.strip('\n'))
                    initial_tape = tape.Tape(*turing_tape.group(2).strip(')(').split(','))
                    line_counter += 1
                elif re.match(initial_regex, line.strip('\n')) != None:
                    turing_initial = re.match(initial_regex, line.strip('\n'))
                    initial_state = int(turing_initial.group(2))
                else:
                    line_counter += 1
                    raise SyntacticError("Syntactic error on line %d" %
                                         line_counter, line.strip('\n'))
    except SyntacticError as error:
        print(error.message)
        print('More specifically, the error lies within:\n', error.messed_line)
        raise  
    return TuringMachine(initial_tape,states,accept_states,reject_states,initial_state,*machine_rules)
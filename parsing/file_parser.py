import sys
import re


class SyntacticError(Exception):

    def __init__(self, message, messed_line=5):
        self.message = message
        self.messed_line = messed_line


machine_rules = []
states = set()
accept_states = set()
reject_states = set()


rule_regex = r'^\([0-9]{1,},.,.,.,[0-9]{1,},(Left|None|Right)\)$'
states_regex = r'^(states:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
accept_regex = r'^(accept:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
reject_regex = r'^(reject:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
initial_regex = r'^(initial:\s*)([0-9]*)$'
tape_regex = r'^(tape:\s*)(\((.)*,(.)*,(.)*\))$'


def parse_tape_from_file(file_tape, line_counter):
    tape = re.match(tape_regex, file_tape.strip('\n'))
    if tape is None:
        return SyntacticError('There is syntactic error \
                                with this tape !', line_counter)
    else:
        return tape.group(2).strip(')(').split(',')


def parse_states_from_file(file_states, line_counter):
    states = re.match(states_regex, file_states.strip('\n'))
    if states is None:
        return SyntacticError('There is syntactic error \
                                with these states !', line_counter)
    else:
        machine_states = set()
        for state in states.group(2).strip('}').split(','):
            machine_states.add(int(state))
        return machine_states


def parse_accept_states_from_file(file_accept_states, line_counter):
    accept_states = re.match(accept_regex, file_accept_states.strip('\n'))
    if accept_states is None:
        return SyntacticError('There is syntactic error with these states !',
                              line_counter)
    else:
        machine_states = set()
        for state in accept_states.group(2).strip('}').split(','):
            machine_states.add(int(state))
        return machine_states


def parse_reject_states_from_file(file_reject_states, line_counter):
    reject_states = re.match(reject_regex, file_reject_states.strip('\n'))
    if reject_states is None:
        return SyntacticError('There is syntactic error with these states !',
                              line_counter)
    else:
        machine_states = set()
        for state in reject_states.group(2).strip('}').split(','):
            machine_states.add(int(state))
        return machine_states


def parse_initial_from_file(file_initial_state, line_counter):
    initial = re.match(initial_regex, file_initial_state.strip('\n'))
    if initial is None:
        return SyntacticError('There is syntactic error \
                                with the initial state !', line_counter)
    else:
        return int(initial.group(2))


def parse_rule_from_file(file_rule, line_counter):
    file_rule = re.match(rule_regex, file_rule)
    if file_rule is None:
        return SyntacticError('There is syntactic error with this rule !',
                              line_counter)
    else:
        rule = file_rule.group().strip('\n)(').split(',')
        rule[0] = int(rule[0])
        rule[4] = int(rule[4])
    return rule


def parse_validator_from_file(program_name=None):
    line_counter = 1
    stack = ''
    try:
        with open(program_name, "rt") as program:
            for line in program:
                if line == '\n' or line.strip('\n')[0] == '#':
                    line_counter += 1
                    continue
                line = re.sub(r'#.*', '', line)
                if line[0] == '(':
                    rule = parse_rule_from_file(line, line_counter)
                    machine_rules.append(rule)
                    line_counter += 1
                elif line[0] == 't':
                    tape = parse_tape_from_file(line, line_counter)
                    line_counter += 1
                elif line[:5] == 'stack':
                    stack = line[6:-1]
                    line_counter += 1
                elif line[0] == 's':
                    states = parse_states_from_file(line, line_counter)
                    line_counter += 1
                elif line[0] == 'a':
                    accept_states = parse_accept_states_from_file(
                        line, line_counter)
                    line_counter += 1
                elif line[0] == 'r':
                    reject_states = parse_reject_states_from_file(
                        line, line_counter)
                    line_counter += 1
                elif line[0] == 'i':
                    initial_state = parse_initial_from_file(line, line_counter)
                    line_counter += 1
                else:
                    raise SyntacticError('There is syntactic error.', line_counter)
    except SyntacticError as error:
        print(error.message)
        print('More specifically, the error lies within:\n', error.messed_line)
        raise
    return (tape, states, accept_states, reject_states,
            initial_state, stack, machine_rules)

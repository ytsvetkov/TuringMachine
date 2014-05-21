import sys
import re
import rule


machine_rules = []
states = set()
accept_states = set()
reject_states = set()


rule_regex = r'^\([0-9]{1,},.,.,[0-9]{1,},(Left|None|Right)\)$'
states_regex = r'^(states:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
accept_regex = r'^(accept:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'
reject_regex = r'^(reject:\s*){(}|([0-9]*,)*[0-9]*}|[0-9]*})$'


with open(sys.argv[1], "rt") as program:
    for line in program:
        if line == '\n': continue
        elif re.match(rule_regex, line.strip('\n')):
            turing_rule = line.strip('\n)(').split(',')
            machine_rules.append(rule.Rule(*turing_rule))
        elif re.match(states_regex, line.strip('\n')) != None:
            turing_states = re.match(states_regex, line.strip('\n'))
            for state in turing_states.group(2).strip('}').split(','):
                states.add(int(state))
        elif re.match(accept_regex, line.strip('\n')) != None:
            turing_accept = re.match(accept_regex, line.strip('\n'))
            for state in turing_accept.group(2).strip('}').split(','):
                accept_states.add(int(state))
        elif re.match(reject_regex, line.strip('\n')) != None:
            turing_reject = re.match(reject_regex, line.strip('\n'))
            for state in turing_reject.group(2).strip('}').split(','):
                reject_states.add(int(state))


import tape
import rule
import rule_book


class TuringMachine:

    def __init__(self, tape, states, accept_states, reject_states, current_state, *rules):
        self.tape = tape
        self.correct_states(states, accept_states, reject_states, current_state)
        self.states = set(states)
        self.accept_states = set(accept_states)
        self.reject_states = set(reject_states)
        self.current_state = current_state
        self.head = self.tape.middle
        self.rules = rule_book.Rule_Book(*rules)

    def __repr__(self):
        return '{}-{}-{}-{}-{}-{}'.format(self.tape, self.states, self.accept_states, self.rules, self.current_state, self.head)

    def correct_states(self, states, final_states, reject_states, current_state):
        if not final_states in states and reject_states in states and\
                set(final_states).intersection(set(reject_states)):
            raise TypeError

    def run(self):
        print(self.tape)
        while (self.current_state not in self.accept_states) or (self.current_state not in self.reject_states):
            read_character = self.tape.read()
            if self.rules.can_be_applied(self.current_state, read_character):
                rule_to_apply = self.rules.get_rule(self.current_state, read_character)
                self.tape.write(rule_to_apply.write_character)
                if rule_to_apply.direction == 'Left':
                    self.tape.move_head_left()
                elif rule_to_apply.direction == 'Right':
                    self.tape.move_head_right()
                elif not rule_to_apply.direction == 'None':
                    raise TypeError
                self.current_state = rule_to_apply.next_state
            else:
                break
            print(self.tape)
        if self.current_state in self.accept_states:
            print(self.tape)
            return 'accept'
        elif self.current_state in self.reject_states:
            print(self.tape)
            return 'reject'


aa = []

aa.append(rule.Rule(0,'a','_',1,'Right'))
aa.append(rule.Rule(0,'b','_',2,'Right'))
aa.append(rule.Rule(0,'_','_',5,'Left'))

aa.append(rule.Rule(1,'a','a',1,'Right'))
aa.append(rule.Rule(1,'b','b',1,'Right'))
aa.append(rule.Rule(1,'_','_',3,'Left'))

aa.append(rule.Rule(2,'a','a',2,'Right'))
aa.append(rule.Rule(2,'b','b',2,'Right'))
aa.append(rule.Rule(2,'_','_',4,'Left'))

aa.append(rule.Rule(3,'a','_',7,'Left'))
aa.append(rule.Rule(3,'b','b',6,'Left'))
aa.append(rule.Rule(3,'_','_',5,'Left'))

aa.append(rule.Rule(4,'a','a',6,'Left'))
aa.append(rule.Rule(4,'b','_',7,'Left'))
aa.append(rule.Rule(4,'_','_',5,'Left'))

aa.append(rule.Rule(5,'a','a',5,'Right'))
aa.append(rule.Rule(6,'b','b',6,'Right'))

aa.append(rule.Rule(7,'a','a',7,'Left'))
aa.append(rule.Rule(7,'b','b',7,'Left'))
aa.append(rule.Rule(7,'_','_',0,'Right'))

states = {0,1,2,3,4,5,6,7}
astates = {5}
rstates = {6}

x = tape.Tape(' ', 'b', 'ababaabbbaababab')
y=TuringMachine(x,states,astates,rstates,0,*aa)
print(y.run())
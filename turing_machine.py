import tape
import rule
import rule_book


class TuringMachine:

    def __init__(self, tapee, states, accept_states, reject_states, current_state, *rules):
        self.tapee = tapee
        self.correct_states(states, accept_states,
                            reject_states, current_state)
        self.states = set(states)
        self.accept_states = set(accept_states)
        self.reject_states = set(reject_states)
        self.current_state = current_state
        self.head = self.tapee.middle
        self.rules = rule_book.Rule_Book(*rules)

    def __repr__(self):
        return '{}-{}-{}-{}-{}-{}'.format(self.tapee, self.states,
                                          self.accept_states, self.rules,
                                          self.current_state, self.head)

    def __eq__(self, other):
        return self.tapee == other.tape and self.states == other.states and\
        self.accept_states == other.accept_states and self.reject_states == other.reject_states and\
        self.current_message == other.current_state and self.head == other.head and self.rules == other.rules

    def correct_states(self, states, final_states, reject_states, current_state):
        if not final_states in states and reject_states in states and\
                set(final_states).intersection(set(reject_states)):
            raise TypeError

    def run(self):
        print(self.tapee, "Initial tape", self.current_state)
        while (self.current_state not in self.accept_states) or (self.current_state not in self.reject_states):
            read_character = self.tapee.read()
            if self.rules.can_be_applied(self.current_state, read_character):
                rule_to_apply = self.rules.get_rule(
                    self.current_state, read_character)
                self.tapee.write(rule_to_apply.write_character)
                if rule_to_apply.direction == 'Left':
                    self.tapee.move_head_left()
                elif rule_to_apply.direction == 'Right':
                    self.tapee.move_head_right()
                elif not rule_to_apply.direction == 'None':
                    raise TypeError
                self.current_state = rule_to_apply.next_state
            else:
                break
            print(self.tapee, self.current_state)
        if self.current_state in self.accept_states:
            return 'accept'
        elif self.current_state in self.reject_states:
            return 'reject'

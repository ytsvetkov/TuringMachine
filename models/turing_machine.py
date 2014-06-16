import os
import sys
sys.path.append(os.getcwd())
from models import rule
from models import rule_book
from models import tape as _tape
from collections import deque


class StateError(Exception):

    def __init__(self, message):
        self.message = message


class Stack(deque):

    def __str__(self):
        return 'stack{}'.format(self.__repr__()[5:])


class TuringMachine:

    def __init__(self, tape, states, accept_states,
                 reject_states, current_state, stack, rules):
        self.correct_states(states, accept_states,
                            reject_states, current_state)
        self.tape = _tape.Tape(*tape)
        self.states = set(states)
        self.accept_states = set(accept_states)
        self.reject_states = set(reject_states)
        self.current_state = current_state
        self.head = self.tape.middle
        self.stack = Stack() if stack is None else Stack(stack)
        self.rules = rule_book.Rule_Book(rules)

    def __repr__(self):
        return '{}-{}-{}-{}-{}-{}-{}'.format(self.tape, self.states, self.stack,
                                          self.accept_states, self.rules,
                                          self.current_state, self.head)

    def __eq__(self, other):
        return self.tape == other.tape and self.states == other.states and\
            self.stack == other.stack and\
            self.accept_states == other.accept_states and\
            self.reject_states == other.reject_states and\
            self.current_state == other.current_state and\
            self.head == other.head and self.rules == other.rules

    def correct_states(self, states, accept_states,
                       reject_states, current_state):
        if set(accept_states).intersection(set(states)) == set():
            raise StateError('Accept states not in "States" !')
        elif set(reject_states).intersection(set(states)) == set():
            raise StateError('Accept states not in "States" !')
        elif set([current_state]).intersection(set(states)) == set():
            raise StateError('Initial states not in "States" !')
        elif set(accept_states).intersection(set(reject_states)):
            raise StateError('Can\'t have state both accept and reject !')

    def run(self):
        print()
        print(self.tape)
        print(self.stack)
        applied_rule = self.step()
        if applied_rule is None:
            return '\nYour machine halted !!!\n'
        while (self.current_state not in self.accept_states) and\
                (self.current_state not in self.reject_states):
            print('Rule to be applied: ', applied_rule, '\n')
            print(self.tape)
            print(self.stack)
            applied_rule = self.step()
        print(applied_rule)

        if self.current_state in self.accept_states:
            return '\nYour word is accepted !!!\n'
        elif self.current_state in self.reject_states:
            return '\nYour word is rejected !!!\n'


    def step(self):
        if self.current_state in self.accept_states:
            return 'accept'
        elif self.current_state in self.reject_states:
            return 'reject'

        read_character = self.tape.read()
        if self.rules.can_be_applied(self.current_state, read_character):
            rule_to_apply = self.rules.get_rule(
                self.current_state, read_character)
            self.tape.write(rule_to_apply.write_character)
            if rule_to_apply.stack_character == '^':
                self.stack.popleft()
            elif rule_to_apply.stack_character == '_':
                pass
            else:
                self.stack.appendleft(rule_to_apply.stack_character)
            if rule_to_apply.direction == 'Left':
                self.tape.move_head_left()
            elif rule_to_apply.direction == 'Right':
                self.tape.move_head_right()
            elif not rule_to_apply.direction == 'None':
                raise TypeError
            self.current_state = rule_to_apply.next_state
        else:
            return
        return rule_to_apply
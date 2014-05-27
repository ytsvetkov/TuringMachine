import sys
import re
import rule as _rule
import tape as _tape
import turing_machine


def machine_builder(tape, states, accept_states,
                    reject_states, initial_state, rules):
    return turing_machine.TuringMachine(tape, states, accept_states,
                                        reject_states, initial_state,
                                        rules)
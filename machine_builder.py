import sys
import re
from models import rule as _rule
from models import tape as _tape
from models import turing_machine


def machine_builder(tape, states, accept_states,
                    reject_states, initial_state, rules):
    return turing_machine.TuringMachine(tape, states, accept_states,
                                        reject_states, initial_state,
                                        rules)
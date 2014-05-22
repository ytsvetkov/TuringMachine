import sys
import re
import rule
import tape
import turing_machine

def machine_builder(tapee, statess, accept_statess,
                       reject_statess, initial_statee, ruless):
    rule_book = []
    for rulee in ruless:
        rule_book.append(rule.Rule(*rulee))
    tapeee = tape.Tape(*tapee)
    return turing_machine.TuringMachine(tapeee, statess, accept_statess,
                                        reject_statess, initial_statee,
                                        *rule_book)
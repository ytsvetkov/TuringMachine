class Rule:

    def __init__(self, current_state, read_character, write_character,
                 stack_character, next_state, direction):
        self.read_character = read_character
        self.write_character = write_character
        self.stack_character = stack_character
        self.current_state = current_state
        self.next_state = next_state
        self.direction = direction

    def __repr__(self):
        return '(({}-{})({}-{}-{}-{}))'.format(self.current_state,
                                               self.read_character,
                                               self.write_character,
                                               self.stack_character,
                                               self.next_state,
                                               self.direction)

    def __eq__(self, other):
        return self.read_character == other.read_character and\
            self.write_character == other.write_character and\
            self.current_state == other.current_state and\
            self.next_state == other.next_state and\
            self.direction == other.direction

    def can_be_applied(self, state, read_character):
        return self.current_state == state and\
            self.read_character == read_character

from collections import deque


class Tape:

    empty = '_'

    def __init__(self, left=empty, middle=empty, right=empty):
        self.left = deque(left)
        self.middle = middle
        self.right = deque(right)

    def move_head_right(self):
        self.left.append(self.middle)
        self.middle = self.right.popleft()
        if not self.right:
            self.right.append(Tape.empty)

    def move_head_left(self):
        self.right.appendleft(self.middle)
        if len(self.left) == 0:
            self.middle = self.empty
            self.left.append(self.empty)
        elif len(self.left) == 1:
            self.middle = self.left.popleft()
            self.left.append(self.empty)
        else:
            self.middle = self.left.popleft()

    def read(self):
        return self.middle

    def write(self, symbol):
        self.middle = symbol

    def __eq__(self, other):
        return self.left == other.left and\
            self.middle == other.middle and\
            self.right == other.right

    def __repr__(self):
        return "<Tape {}({}){}>".format(''.join(self.left),
                                        self.middle, ''.join(self.right))

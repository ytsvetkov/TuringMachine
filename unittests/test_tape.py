import unittest
import sys
sys.path.append('/home/thepuppeteer/Projects/Python/Project/models')
from tape import Tape


class TapeTest(unittest.TestCase):

    def test_left_right_move(self):
        test_tape = Tape(['1', '0', '1'], '1', ['0'])
        result_tape = Tape(['1', '0', '1'], '1', ['0'])
        result_tape.move_head_left()
        result_tape.move_head_right()
        self.assertEqual(test_tape, result_tape)

    def test_right_move(self):
        test_tape = Tape(['1', '1', '1', '1'], '0', ['0', '1'])
        result_tape = Tape(['1', '1'], '1', ['1', '0', '0', '1'])
        result_tape.move_head_right()
        result_tape.move_head_right()
        self.assertEqual(test_tape, result_tape)

    def test_left_move(self):
        result_tape = Tape(['1', '1', '1', '1'], '0', ['0', '1'])
        test_tape = Tape(['1', '1'], '1', ['1', '0', '0', '1'])
        result_tape.move_head_left()
        result_tape.move_head_left()
        self.assertEqual(test_tape, result_tape)

    def test_write(self):
        test_tape = Tape(['1', '1', '1', '1'], '0', ['0', '1'])
        result_tape = Tape(['1', '1', '1', '1'], '1', ['0', '1'])
        result_tape.write('0')
        self.assertEqual(test_tape, result_tape)

    def test_write_error(self):
        result_tape = Tape(['1', '1', '1', '1'], '0', ['0', '1'])
        self.assertRaises(TypeError, result_tape.write)


if __name__ == '__main__':
    unittest.main()

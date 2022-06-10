import unittest

from ...homework.block_2_2 import ExcError


class TestExc(unittest.TestCase):

    exceptions = (ValueError, SyntaxError, SystemError)

    def test_wrong_type(self):
        with self.assertRaises(TypeError):
            with ExcError(self.exceptions, 'text.txt', 'r') as exc:
                exc.write(12345)

    def test_wrong_name(self):
        with self.assertRaises(NameError):
            with ExcError(self.exceptions, 'text.txt', 'r') as exc:
                exc.write(a)









from ..block_3 import IOManager
import sys
import unittest


class TestIOManager(unittest.TestCase):

    def test_writing_to_stdout(self):
        with open('stdout.txt', 'w') as stdout:
            with open('stderr.txt', 'w') as stderr:
                with IOManager(stderr, stdout):
                    to_stdout = 'to stdout'
                    print(to_stdout)
                stderr.close()
                stdout.close()
        with open('stdout.txt', 'r') as stdout_read:
            read_file_stdout = stdout_read.read()
            self.assertTrue(to_stdout in read_file_stdout)

    def test_writing_to_stderr(self):
        with open('stdout.txt', 'w') as stdout:
            with open('stderr.txt', 'w') as stderr:
                with IOManager(stderr, stdout):
                    to_stderr = 'to stderr'
                    print(to_stderr, file=sys.stderr)
                stderr.close()
                stdout.close()
        with open('stderr.txt', 'r') as stderr_read:
            read_file_stderr = stderr_read.read()
            self.assertTrue(to_stderr in read_file_stderr)

    def test_writing_exc_to_stderr(self):
        with open('stdout.txt', 'w') as stdout:
            with open('stderr.txt', 'w') as stderr:
                with IOManager(stderr, stdout):
                    10 / 0
                stderr.close()
                stdout.close()
        with open('stdout.txt', 'r') as stdout_read:
            read_file_exc = stdout_read.read()
            self.assertTrue('ZeroDivisionError' in read_file_exc)




import sys


class IOManager:
    def __init__(self, stderr, stdout):
        self.stderr = stderr
        self.stdout = stdout

    def __enter__(self):
        self.stdout_sys_save = sys.stdout
        self.stderr_sys_save = sys.stderr
        sys.stdout = self.stdout
        sys.stderr = self.stderr

    def __exit__(self, type, value, traceback):
        print(f'Exception {type, value}')
        sys.stdout = self.stdout_sys_save
        sys.stderr = self.stderr_sys_save
        return True


with open('stdout.txt', 'w') as stdout:
    with open('stderr.txt', 'w') as stderr:
        with IOManager(stderr, stdout):
            print('to stdout')
            print('to stderr', file=sys.stderr)
            100 + '100'
        stderr.close()
        stdout.close()

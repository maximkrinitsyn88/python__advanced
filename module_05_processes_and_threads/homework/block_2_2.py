class ExcError:
    def __init__(self, exceptions, name, mode='r'):
        self.exceptions = exceptions
        self.name = name
        self.mode = mode

    def __enter__(self):
        self.file = open(self.name, self.mode)
        return self.file

    def __exit__(self, type, value, traceback):
        print(type, value)
        if type in self.exceptions:
            self.file.close()
            return True, type, value


exceptions = (NameError, TypeError, SystemError, ConnectionError, SyntaxError, ValueError)

if __name__ == '__main__':
    with ExcError(exceptions, 'text.txt', 'w') as exc:
        exc.write('Hello')
        with open('ccc.txt', 'w') as ccc:
            ccc.write(a)


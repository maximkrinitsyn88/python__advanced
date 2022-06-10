import sys


def main():
    print('Print to stdout')
    print('Print to stderr', file=sys.stderr)
    name = input()
    patronymic = input()
    surname = input()
    print('User : "{}" "{}" "{}"'.format(name, patronymic, surname))


if __name__ == '__main__':
    main()

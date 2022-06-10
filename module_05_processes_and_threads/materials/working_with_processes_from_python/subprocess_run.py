import subprocess


def run_program():
    subprocess.run(['python', 'test_program.py'], encoding='utf-8', input='Иван\nИванович\nИванов')


if __name__ == '__main__':
    run_program()

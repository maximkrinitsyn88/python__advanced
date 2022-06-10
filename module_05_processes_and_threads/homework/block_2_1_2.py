import os
import signal
import subprocess
import shlex


def run_program(port):
    command_str = f'lsof -i :{port}'
    command = shlex.split(command_str)
    command_run = subprocess.run(command, capture_output=True)
    command_splt = str(command_run.stdout).split(' ')
    for elem in command_splt:
        if elem.isdigit():
            try:
                os.kill(int(elem), signal.SIGKILL)
                print(f'Предыдущий процесс {elem} завершён')
            except:
                print(f'Это не процесс {elem}')
    subprocess.run(['python', 'block_2_1_1.py'], capture_output=True)


if __name__ == '__main__':
    run_program('5000')

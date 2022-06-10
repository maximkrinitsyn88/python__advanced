import subprocess


def popen():
    p = subprocess.Popen('vim')
    return p


if __name__ == '__main__':
    res = popen()


# 1. Запускаю через python console
# 2. Затем приостанавливаю res.wait()
# 3. Прерываю процесс методом res.kill()


# Вторую часть блока смотрите в subprocess_run и test_program.py
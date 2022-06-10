"""
В своей работе программист должен часто уметь решать рутинные задачи.

Хорошим примером такой задачи является вычисление суммарного размера директории.

Пожалуйста реализуйте функцию, которая на вход принимает путь до папки
    в виде стрки или объекта Path
и возвращает суммарный объём директории в байтах.

В случае, если на вход функции передаётся несуществующий путь или НЕ директория,
    функция должна выкинуть исключение ValueError с красивым описание ошибки
"""
from pathlib import Path
from typing import Union


def calculate_directory_size(directory_path: Union[str, Path] = ".") -> int:
    print(f'Переданный вами путь: {directory_path}')
    home = Path.home()
    size = 0
    try:
        for f in Path(home, directory_path).glob("**/*"):
            size += f.stat().st_size
        if size == 0:
            raise ValueError
    except ValueError:
        print('Вы передали либо: 1. Несуществующий путь \n'
              '                  2. Это не директория \n'
              '                  3. Директория пуста')
    return size


calc_path = calculate_directory_size(Path('OneDrive', 'Рабочий стол', 'Учёба'))
print(f'Размер директории в байтах: {calc_path}')
calc_str = calculate_directory_size('OneDrive/Рабочий стол/Учёба')
print(f'Размер директории в байтах: {calc_str}')
calc_str_second = calculate_directory_size('C:\\Users\\krini\\OneDrive\\Рабочий стол\\Учёба\\Курсы Skillbox\\python_advanced')
print(f'Размер директории в байтах: {calc_str_second}')

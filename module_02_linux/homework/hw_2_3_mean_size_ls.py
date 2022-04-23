"""
Напишите функцию, которая будет по output команды ls возвращать средний размер файла в папке.
$ ls -l ./
В качестве аргумента функции должен выступать путь до файла с output команды ls
"""
import os


def get_mean_size(ls_output_path: str) -> float:
    amount_of_memory = 0
    amount_of_files = 0
    with open(ls_output_path) as ls:
        for line in ls:
            elem = line.split()
            if len(elem) > 2:
                amount_of_files += 1
                amount_of_memory += int(elem[4])
    avg_memory = amount_of_memory / amount_of_files
    return avg_memory


if __name__ == "__main__":
    print(get_mean_size("out.txt"))

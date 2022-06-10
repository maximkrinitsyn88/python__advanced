"""
Представьте что мы решаем задачу следующего вида.
У нас есть кнопочный телефон (например, знаменитая Нокиа 3310) и мы хотим,
чтобы пользователь мог проще отправлять SMS.

Мы реализуем свой собственный клавиатурный помощник.
Каждой цифре телефона соответствует набор букв:
2 - a ,b, c
3 - d, e, f
4 - g, h, i
5 - j, k, l
6 - m, n, o
7 - p, q, r, s
8 - t, u, v
9 - w, x, y, z

Пользователь нажимает на клавиши, например,  22736368
    после чего на экране печатается basement

Напишите функцию-помощник my_t9, которая на вход принимает цифровую
строку и возвращает list из слов английского языка,
которые можно получить из этой цифровой строки.

В качестве словаря английского языка можете использовать
содержимое файла /usr/share/dict/words

Ваше решение должно работать с алгоритмической сложностью O(N),
где N -- длина цифровой строки.
"""
from typing import List
import itertools

letters = {
    2: ['a', 'b', 'c'],
    3: ['d', 'e', 'f'],
    4: ['g', 'h', 'i'],
    5: ['j', 'k', 'l'],
    6: ['m', 'n', 'o'],
    7: ['p', 'q', 'r', 's'],
    8: ['t', 'u', 'v'],
    9: ['w', 'x', 'y', 'z']
}


def my_t9(input_numbers: str) -> List[str]:
    all_letters = []
    t9_words = []
    for numb in input_numbers:
        possible_letter = letters[int(numb)]
        all_letters.append(possible_letter)
    words = list(itertools.product(*all_letters))
    with open('/usr/share/dict/words', 'r') as eng_words:
        file_words = eng_words.read()
        for letter in words:
            word = ''.join(letter)
            if word in file_words:
                t9_words.append(word)
    return t9_words


t9 = my_t9('22736368')
print(t9)

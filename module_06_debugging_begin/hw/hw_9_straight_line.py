"""
Давайте немного отойдём от логирования.
Программист должен знать не только computer science, но и математику.
Давайте вспомним школьный курс математики.

Итак, нам нужно реализовать функцию, которая принимает на вход
list из координат точек (каждая из них - tuple с x и y).

Напишите функцию, которая определяет, лежат ли все эти точки на одной прямой или не лежат
"""
from typing import List, Tuple


def check_is_straight_line(coordinates: List[Tuple[float, float]]) -> bool:
    n = 0
    while len(coordinates):
        try:
            x1 = coordinates[n][0]
            x2 = coordinates[n+1][0]
            x3 = coordinates[n+2][0]
            y1 = coordinates[n][1]
            y2 = coordinates[n+1][1]
            y3 = coordinates[n+2][1]
            a = (x1 - x2) * (y3 - y2)
            b = (x3 - x2) * (y1 - y2)
            if a == b:
                print(f'Точки {(x1,y1),(x2,y2),(x3,y3)} лежат на одной прямой')
            else:
                print(f'Точки {(x1,y1),(x2,y2),(x3,y3)} не лежат на одной прямой')
                return False
            n += 1
        except IndexError:
            print('Точки для сравнения закончились')
            break
    return True


res = check_is_straight_line([(-2, -7), (-1, -4), (5, 14), (8, 2), (-2, -7), (-1, -4), (5, 14)])
print(res)



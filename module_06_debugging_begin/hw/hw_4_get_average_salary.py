"""
Вы работаете программистом на предприятии.
К вам пришли из бухгалтерии и попросили посчитать среднюю зарплату по предприятию.
Вы посчитали, получилось слишком много, совсем не реалистично.
Вы подумали и проконсультировались со знакомым из отдела статистики.
Он посоветовал отбросить максимальную и минимальную зарплату.
Вы прикинули, получилось что-то похожее на правду.

Реализуйте функцию get_average_salary_corrected,
которая принимает на вход непустой массив заработных плат
(каждая -- число int) и возвращает среднюю з/п из этого массива
после отбрасывания минимальной и максимальной з/п.

Задачу нужно решить с алгоритмической сложностью O(N) , где N -- длина массива зарплат.

Покройте функцию логгированием.
"""
import logging
from typing import List

logger = logging.getLogger('salary-log')


def get_average_salary_corrected(salaries: List[int]) -> float:
    logger.debug('Начало get_average_salary_corrected')
    summ_salary = 0
    max_numb = salaries[0]
    min_numb = salaries[0]
    for numb in salaries:
        summ_salary += numb
        if numb > max_numb:
            logger.info(f'Максимальное число переопределено. Оно равно: {numb}')
            max_numb = numb
        elif numb < min_numb:
            logger.info(f'Минимальное число переопределено. Оно равно: {numb}')
            min_numb = numb
    return (summ_salary - max_numb - min_numb) / len(salaries)


if __name__ == "__main__":
    logging.basicConfig(level=logging.DEBUG)
    logger.info("Найдем среднюю ЗП")
    avg_salary = get_average_salary_corrected([2, 3, 4, 5, 12, 7, 8, 9, 2, 1])
    logger.info(f'Средняя заработная плата: {avg_salary}')

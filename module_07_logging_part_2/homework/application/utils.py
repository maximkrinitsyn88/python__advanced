import logging
import logging.config
from typing import Union, Callable
from operator import sub, mul, truediv, add


utils_logger = logging.getLogger('utils_logger')


OPERATORS = {
    '+': add,
    '-': sub,
    '*': mul,
    '/': truediv
}

Numeric = Union[int, float]


def string_to_operator(value: str) -> Callable[[Numeric, Numeric], Numeric]:
    utils_logger.info(f'Check operator: {value}')
    """
    Convert string to arithmetic function
    :param value: basic arithmetic function
    """
    if not isinstance(value, str):
        utils_logger.exception('wrong operator type', value)
        raise ValueError("wrong operator type")

    if value not in OPERATORS:
        utils_logger.exception('wrong operator type', value)
        raise ValueError("wrong operator value")

    return OPERATORS[value]

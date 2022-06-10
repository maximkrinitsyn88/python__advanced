import logging
import sys
import re
import logging.config
from logging_tree import printout
from utils import string_to_operator
from app_logger_config import app_logger_config

app_logger = logging.getLogger('app_logger')


def calc(args):
    app_logger.info(f'Arguments: {args}')

    num_1 = args[0]
    operator = args[1]
    num_2 = args[2]

    try:
        num_1 = float(num_1)
    except ValueError as e:
        app_logger.exception("Error while converting number 1")
        app_logger.exception(e)

    try:
        num_2 = float(num_2)
    except ValueError as e:
        app_logger.exception("Error while converting number 2")
        app_logger.exception(e)

    operator_func = string_to_operator(operator)

    result = operator_func(num_1, num_2)

    app_logger.info(f'Result: {result}')
    app_logger.info(f"{num_1} {operator} {num_2} = {result}")


def configuration():
    class CustomFilter(logging.Filter):

        def filter(self, record):
            only_ascii = r'^[\x00-\x7F]+$'
            ascii_str = re.search(only_ascii, str(record))
            if ascii_str:
                return True
            else:
                return False

    # app_logger.addFilter(CustomFilter())
    # logging.config.dictConfig(app_logger_config)
    logging.config.fileConfig('app_logger_config_ini.ini')


if __name__ == '__main__':
    configuration()
    calc(sys.argv[1:])
    printout()

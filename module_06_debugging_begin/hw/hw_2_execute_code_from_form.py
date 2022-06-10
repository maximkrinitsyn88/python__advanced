"""
Ещё раз рассмотрим Flask endpoint, принимающий код на питоне и исполняющий его.
1. Напишите для него Flask error handler,
    который будет перехватывать OSError и писать в log файл exec.log
    соответствую ошибку с помощью logger.exception
2. Добавьте отдельный exception handler
3. Сделайте так, что в случае непустого stderr (в программе произошла ошибка)
    мы писали лог сообщение с помощью logger.error
4. Добавьте необходимые debug сообщения
5. Инициализируйте basicConfig для записи логов в stdout с указанием времени
"""

import logging
import shlex
import subprocess

from typing import Optional
from flask import Flask
from flask_wtf import FlaskForm
from wtforms import IntegerField, StringField
from wtforms.validators import InputRequired
from werkzeug.exceptions import InternalServerError


logger = logging.getLogger('python_code_check')
app = Flask(__name__)


class CodeForm(FlaskForm):
    code = StringField(validators=[InputRequired()])
    timeout = IntegerField(default=10)


def run_python_code_in_subprocess(code: str, timeout: int) -> str:
    logger.debug('Начало run_python_code_in_subprocess')
    command = f'python3 -c "{code}"'
    command = shlex.split(command)
    process = subprocess.Popen(
            command,
            stdout=subprocess.PIPE,
            stderr=subprocess.PIPE,
    )

    outs, errs = process.communicate(timeout=timeout)

    return outs.decode()


@app.route("/run_code", methods=["POST"])
def run_code():
    form = CodeForm()
    if form.validate_on_submit():
        logger.info('Ваши поля формы действительны')
        code = form.code.data
        timeout = form.timeout.data
        stdout = run_python_code_in_subprocess(code=code, timeout=timeout)
        return f"Stdout: {stdout}"

    return f"Bad request. Error = {form.errors}", 400


@app.errorhandler(InternalServerError)
def handler_exc(e: InternalServerError):
    exception: Optional[Exception] = getattr(e, 'original_exception', None)
    if isinstance(exception, FileNotFoundError):
        with open('exec.log', 'a', encoding='utf-8') as exc:
            exc.write(f'Filename - {exception.filename}, Error - {exception.strerror}\n')
    if isinstance(exception, OSError):
        with open('exec.log', 'a', encoding='utf-8') as exc:
            exc.write(f'Filename - {exception.filename}, Error - {exception.strerror}\n')
    logger.error(f'Наша программа слегла с ошибкой:{exception}')
    return 'Error', 500


if __name__ == "__main__":
    logging.basicConfig(filename='stdout.log', level=logging.DEBUG,
                        format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', datefmt='%H:%M:%S')
    app.config["WTF_CSRF_ENABLED"] = False
    app.run()

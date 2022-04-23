"""
Давайте немного вспомним Linux command line утилиты.

Напишите Flask GET endpoint, который на вход принимает флаги командной строки,
    а возвращает результат запуска команды PS с этими флагами.
    Чтобы красиво отформатировать результат вызова программы - заключите его в тэг <pre>:
        <pre>Put your text here</pre>

Endpoint должен быть по url = /ps и принимать входные значение через аргумент arg
Напомню, вызвать программу ps можно, например, вот так

"""
import shlex
import subprocess

from flask import Flask, request
from typing import List
app = Flask(__name__)


@app.route("/ps/", methods=["GET"])
def _ps():
    flags: List[str] = request.args.getlist('flag', type=str)
    clean_flags = [shlex.quote(flag) for flag in flags]
    command_str = f"ps {' '.join(clean_flags)}"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    if result.returncode != 0:
        return 'Error'
    out = result.stdout.decode()
    return f'<pre>{str(out)}<pre>'


if __name__ == "__main__":
    app.run(debug=True)

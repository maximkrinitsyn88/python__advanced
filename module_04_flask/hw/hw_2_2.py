"""
Напишите GET flask endpoint с url /uptime,
    который в ответ на запрос будет возвращать как долго текущая машина не перезагружалась
        (в виде строки f"Current uptime is '{UPTIME}'"
            где UPTIME - uptime системы. Это можно сделать с помощью команды uptime
            (https://www.opennet.ru/man.shtml?topic=uptime&category=1&russian=4)
        )

Напомним, что вызвать программу из python можно с помощью модуля subprocess:
"""

from flask import Flask
import shlex
import subprocess

app = Flask(__name__)


@app.route("/uptime", methods=["GET"])
def uptime():
    command_str = f"uptime"
    command = shlex.split(command_str)
    result = subprocess.run(command, capture_output=True)
    result_str = str(result).split(' ')
    time = (result_str[5] + result_str[6])[:-1]
    return str(time)


if __name__ == "__main__":
    app.run(debug=True)

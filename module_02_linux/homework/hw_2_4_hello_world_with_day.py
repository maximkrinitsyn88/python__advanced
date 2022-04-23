"""
Напишите  hello-world endpoint , который возвращал бы строку "Привет, <имя>. Хорошей пятницы!".
Вместо хорошей пятницы, endpoint должен уметь желать хорошего дня недели в целом, на русском языке.
Текущий день недели можно узнать вот так:
"""

import datetime

from flask import Flask

app = Flask(__name__)


@app.route("/hello-world/<name>")
def hello_world(name):
    days = ['Понедельник', 'Вторник', 'Среда', 'Четверг', 'Пятница', 'Суббота', 'Воскресенье']
    day = datetime.datetime.today().weekday()
    return f'Привет, {name}. Хорошей {days[day]}'


if __name__ == "__main__":
    app.run(debug=True)

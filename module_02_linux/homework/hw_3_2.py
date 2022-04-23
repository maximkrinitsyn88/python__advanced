"""
Давайте напишем свое приложение для учета финансов.
Оно должно уметь запоминать, сколько денег мы потратили за день,
    а также показывать затраты за отдельный месяц и за целый год.

Модифицируйте  приведенный ниже код так, чтобы у нас получилось 3 endpoint:
/add/<date>/<int:number> - endpoint, который сохраняет информацию о совершённой за какой-то день трате денег (в рублях, предполагаем что без копеек)
/calculate/<int:year> -- возвращает суммарные траты за указанный год
/calculate/<int:year>/<int:month> -- возвращает суммарную трату за указанный месяц

Гарантируется, что дата для /add/ endpoint передаётся в формате
YYYYMMDD , где YYYY -- год, MM -- месяц (число от 1 до 12), DD -- число (от 01 до 31)
Гарантируется, что переданная дата -- корректная (никаких 31 февраля)
"""
from flask import Flask

app = Flask(__name__)

storage = {}

months = {
    1: 31,
    2: 28,
    3: 31,
    4: 30,
    5: 31,
    6: 30,
    7: 31,
    8: 31,
    9: 30,
    10: 31,
    11: 30,
    12: 31
}


@app.route("/add/<date>/<int:number>")
def add(date: str, number: int):
    global storage
    if len(date) == 8:
        month = date[4:6]
        day = date[6:8]
        month = int(month)
        if month in months.keys():
            days_in_month = months[month]
            if 1 <= int(day) < days_in_month:
                storage.update({date: number})
                return storage
            else:
                raise Exception('В этом месяце нет такого дня')
        else:
            raise Exception('Нет такого месяца')
    else:
        raise Exception('Некорректная дата')


@app.route("/calculate/<int:year>")
def calculate_year(year: int) -> str:
    money_year = 0
    for day, money in storage.items():
        if year == int(day[0:4]):
            money_year += storage[day]
    return f'Суммарные траты за {year} год: {money_year}'


@app.route("/calculate/<int:year>/<int:month>")
def calculate_month(year: int, month: int) -> str:
    money_month = 0
    for day, money in storage.items():
        if year == int(day[0:4]) and month == int(day[4:6]):
            money_month += storage[day]
    month = str(month)
    if len(month) == 1:
        month = '0' + month
    return f'Суммарные траты за {str(month)} месяц: {money_month}'


if __name__ == "__main__":
    app.run(debug=True)

import datetime
import random
from flask import Flask

app = Flask(__name__)
counter = 0


@app.route('/hello_world')
def hello_function():
   return 'Привет, мир!'


@app.route('/cars')
def cars_function():
   return "Chevrolet, Renault, Ford, Lada"


@app.route('/cats')
def cats_function():
   cats = ['корниш рекс', 'русская голубая', 'шотландская вислоухая', 'мейн-кун', 'манчкин']
   return random.choice(cats)


@app.route('/get_time/now')
def get_time_function():
   current_time = datetime.datetime.now()
   return f'Точное время {current_time}'


@app.route('/get_time/future')
def future_function():
   current_time_after_hour = datetime.datetime.now() + datetime.timedelta(hours=1)
   return f"Точное время через час будет {current_time_after_hour}"


@app.route('/get_random_word')
def random_word_function():
   with open(file='war_and_peace.txt', encoding='utf-8') as wap:
      words = wap.read().split()
      return random.choice(words)


@app.route('/counter')
def counter_function():
   global counter
   counter += 1
   return str(counter)

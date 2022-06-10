"""
Логов бывает очень много. А иногда - ооооооооочень много.
Из-за этого люди часто пишут логи не в человекочитаемом,
    а в машиночитаемом формате, чтобы машиной их было обрабатывать быстрее.

Напишите функцию

def log(level: str, message: str) -> None:
    pass


которая будет писать лог  в файл skillbox_json_messages.log в следующем формате:
{"time": "<время>", "level": "<level>", "message": "<message>"}

сообщения должны быть отделены друг от друга символами переноса строки.
Обратите внимание: наше залогированное сообщение должно быть валидной json строкой.

Как это сделать? Возможно метод json.dumps поможет вам?
"""
import json
import datetime


def log(level: str, message: str) -> None:
    date_time = datetime.datetime.now()
    date_time_str = date_time.strftime("%H:%M:%S")
    log_object = {'time': date_time_str, 'level': level, 'message': message}
    with open('skillbox_json_messages.log', 'a') as skillbox_log:
        skillbox_log.write(json.dumps(log_object, indent=2) + '\n')


log('level', 'message')

# def.Zone test

Задание было реализовано по требованиям в TODO.txt.
Не было выполнено только представление в виде пакета с зависимостями.
Файла с конфигурацией для pylint (если он требовался) я не делал, проверял, запуская `pylint tags_counter`.

Был использован python3.7

Для запуска:
 1) создать виртуальное окружение (в папке проекта):
 - `python3.7 -m venv venv`
 - `source venv/bin/activate`
 - `pip install -r requirements.txt`
 2) на localhost должен быть запущен Redis
 3) запустить Celery:
 - `REDIS_PASSWORD=<redis_password> PYTHONPATH=<path_to_tags_counter_project> celery -A tags_counter worker --loglevel=info --concurrency=4`
 4) запустить приложение:
 - `REDIS_PASSWORD=<redis_password> python3.7 app.py`
 
Запуск тестов:
Из корневого каталога выполнить `pytest` 
 
В приложении - два API-метода:
 - POST /tags {'url': <url>}
   возвращает id
 - GET /tags/<id>
   возвращает словарь с html-тэгами

подробнее - в TODO.txt

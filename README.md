# Тестовое задание от Mainslab

# Задание
 REST Api using Django rest framework

Реализовать REST API используя DRF

    эндпоинт реализующий отправку email(реально отправлять email не нужно).
    эндпоинт возвращающий инфо по отправленным email
    - адресат
    - тема письма
    - дата отправки
    эндопинт со статистикой по отправленным email за последние 24 часа
    - общее кол-во отправленных
    - топ10 адресатов

В качестве бд можно использовать SQLite. Ответы в формате JSON.


# Решение

запуск
```

env\Scripts\activate
cd rest_api_test_task
python manage.py runserver

```

генерации БД
```
pip install -r requirements.txt
```
```
python manage.py generate_letters 

```


# API

все письма
```
http://127.0.0.1:8000/letters/?format=json
```
топ 10 адресатов за последние сутки
```
http://127.0.0.1:8000/stat_24/?format=json
```



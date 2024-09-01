# *Курсовой проект «Атомные привычки»*

![Python](https://img.shields.io/badge/Python-3.11-f8fc00?logo=python)
![Django](https://img.shields.io/badge/Django-4.2.6-0c730a?logo=django)
![Redis](https://img.shields.io/badge/Redis-5.0.1-red?logo=redis)
![PostgreSQL](https://img.shields.io/badge/PostgreSQL-15.6-blue?logo=postgresql)
![Celery](https://img.shields.io/badge/Celery-5.3.4-green?logo=celery)
![DRF](https://img.shields.io/badge/DRF-3.14.0-0c730a?logo=django)
![JWT](https://img.shields.io/badge/JWT-2.8.0-silver?logo=jsonwebtokens)
![Requests](https://img.shields.io/badge/Requests-2.31.0-3d9ee3?logo=python)
![Eventlet](https://img.shields.io/badge/Eventlet-0.33.3-c44747?logo=eventbrite)

## Цель проекта:

Создание Telegram-бота, который будет уведомлять пользователя о необходимости выполнить то или иное действие
и таким образом позволит выработать полезные привычки.


## Перед началом работы:

- Скачайте в домашнюю директорию.


- Создайте виртуальное окружение venv командой:

__*python -m venv venv*__

- Активируйте виртуальное окружение командой:

__*venv\Scripts\activate.bat*__

- Для Windows - установите и запустите в дополнительном окне WSL2. Информация по установке:

https://learn.microsoft.com/en-us/windows/wsl/install

- Установите зависимости командой:

__*pip install -r requirements.txt*__

- Создайте миграции командами:

__*python manage.py makemigrations*__

__*python manage.py migrate*__

- Создайте Базу Данных (в данном проекте используется PostgreSQL). В базу данных Пользователей вносите ваш username 
в Telegram.


- Перейдите в файл '.env.sample'. Заполните в этом файле все необходимые поля, создайте в директории проекта файл '.env' и перенесите 
туда заполненный в '.env.sample' шаблон. 

Ниже приведен пример заполнения:
```ini
SECRET_KEY = 'your-personal-secret-key'
DEBUG = True/False

DATABASE_NAME = 'name_of_your_database'
DATABASE_USER = 'your_database_username'
DATABASE_PASSWORD = 'your_password_from_the_database'
DATABASE_HOST = '10.255.255.10'
DATABASE_PORT = 5432

TELEGRAM_URL_BOT = 'https://api.telegram.org/bot'
TELEGRAM_API_TOKEN = '111222356:QWE-RTY1234UiO-iD1r46OT4i'

CELERY_BROKER_URL = 'https://10.10.10.10:32/0'
CELERY_RESULT_BACKEND = 'https://10.10.10.00:32/0'
```

## Интеграция с __Telegram__

Для полноценной работы сервиса необходим реализовать работу с отложенными задачами для напоминания о том, в какое время какие привычки необходимо выполнять.

Для этого потребуется интегрировать сервис с мессенджером Telegram, который будет заниматься рассылкой уведомлений.

- Для создания Telegram-бота найдите в чате самого главного бота: [BotFather](https://t.me/BotFather).


- Далее следуйте инструкциям и по завершении создания бота вам будет выдан токен. Его необходимо перенести в 
файл .env в поле __TELEGRAM_API_TOKEN__. Токен будет использован ботом для обращения к API Telegram-сервисов.


----

- Необходимо зайти в файл __*habit_tracker/habit_app/telegram.py*__ и запустить его. Переходите в Telegram-бота и 
нажмите на команду __*/info*__. Внесите предоставленный __*Chat_ID*__ в базу данных в соответствующее поле для того 
пользователя Telegram, с которого вы нажимали на кнопку __*/info*__.

## Работа программы

- __Авторизуйтесь и наполните БД Привычек необходимыми данными.__ Соблюдайте рекомендации:

  - У привычки не может быть связанной привычки и вознаграждения.
  - У приятной привычки не может ни вознаграждения, ни связанной привычки.
  - Связанной привычкой может быть только приятная привычки.
  - Время выполнения должно быть не больше 120 секунд.
  - Периодичность выполнения должно быть не реже, чем 1 раз в 7 дней.


- Откройте в дополнительном окне терминала WSL и запустите Redis, выполнив команду:

`sudo service redis-server start`

- Откройте дополнительное окно терминала и выполните команду:

`celery -A config worker -l INFO -P eventlet`

- Откройте дополнительное окно терминала и выполните команду:

`celery -A config beat -l INFO`

- Запустите сервис командой:

*Windows:*
`python manage.py runserver`

*MacOS / Linux:*
`python3 manage.py runserver`

----

## Завершение работы

Для остановки работы сервера используйте комбинацию клавиш `Ctrl+C` в окне терминала, где он был запущен.

Для остановки работы Celery также используйте `Ctrl+C` в окнах терминала, где запущены команды.

Для остановки работы сервера Redis используйте команду: `sudo service redis-server stop` в окне WSL.

----

## 🐋 Docker: запуск

Для запуска контейнеров в фоновом режиме выполните команду:

`docker-compose up -d --build`

----

## Дополнительная информация

__Покрытие тестами__ (Smoke tests) - 85%

__Документация доступна по ссылке__ (доступно после запуска программы): [Документация](http://127.0.0.1:8000/api/docs/)

Если не удается запустить программу, проверить покрытие тестами и тд, необходимо закомментировать в 
__*habit_tracker/config/settings.py*__ настройки CORS и CSRF, а именно:

- CORS_ALLOWED_ORIGINS

- CSRF_TRUSTED_ORIGINS

- CORS_ALLOW_ALL_ORIGINS.
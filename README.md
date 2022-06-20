# Тестовое задание для компании Numbers

Задание на позицию Разработчик Python / fullstack.

Ссылка на само задание:
**https://soldigital.notion.site/soldigital/developer-5b79683045a64129a2625a19bfb0c944**

Ссылка на таблицу в GoogleSheets:
**https://docs.google.com/spreadsheets/d/10X85OdmyVINkJrY10zbg_y22qLoGYayQQdmWr0kyMOE/edit#gid=0**

Для запуска проекта:

    1) Создайте новую папку/проект.

    2) клонируйте репозиторий.

    3) создайте виртуальное окружение.

    4) установите зависимости из requirements.txt.

**!!!Важно**, если проверяющий использует mac с чипом М1, то перед выполнением следующей команды,
нужно выполнить команду:
    
    export DOCKER_DEFAULT_PLATFORM=linux/amd64
    
если этого не сделать, то при подключении к БД будет пробрасываться ошибка и бот работать не будет:
pg_connect(): Unable to connect to PostgreSQL server: SCRAM authentication requires libpq version 10 or above.
    
    5) выполните команду docker-compose build

    6) выполните команду docker-compose up -d

Docker-compose запустит контейнер с БД и контейнер с ботом
    
    7) найдите в телеграмме бот @numbers_myakotin_test_bot и отправте ему /start

Выполните миграции, для этого 

    6) перейдите в директорию web_numbers в терминале
    
    7) выполните команду ./manage.py migrate

Запустите тестовый сервер

    7) ./manage.py runserver

Откройте в браузере  http://127.0.0.1:8000/ и проверяйте на здоровье.

P:S с надеждой, что в таблицу будут вставляться только валидные данные, 
так как защиту от дурака я не делал :D

С уважением, Максим Мякотин.
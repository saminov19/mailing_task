**Установка и запуск проекта**

***Скопируйте репозиторий проекта с GitHub:***

git clone https://github.com/saminov19/mailing_task.git



***Установите зависимости проекта. Убедитесь, что у вас установлен Python и pip. Из root директории проекта выполните следующую команду:***

pip install -r requirements.txt




***Настройте базу данных. Убедитесь, что у вас установлена совместимая база данных. Обновите конфигурацию базы данных в файле настроек проекта (settings.py) с помощью подходящих учетных данных.***



***Выполните миграции базы данных для создания необходимых таблиц:***

python manage.py migrate




***Загрузите начальные данные, если они доступны:***

python manage.py loaddata <fixture-file>




***Запустите сервер разработки Django:***

python manage.py runserver




***Проект теперь запущен. Обратитесь к конечным точкам API по базовому URL: http://localhost:8000/api/***



**Документация API**
Ниже документированы endpoints API с использованием формата OpenAPI:



Клиенты
POST /api/clients/: Создать нового клиента.
PUT /api/clients/{client_id}/: Обновить атрибуты клиента.
DELETE /api/clients/{client_id}/: Удалить клиента.
Рассылки
POST /api/mailings/: Создать новую рассылку.
GET /api/mailings/{mailing_id}/: Получить подробную статистику для конкретной рассылки.
PUT /api/mailings/{mailing_id}/: Обновить атрибуты рассылки.
DELETE /api/mailings/{mailing_id}/: Удалить рассылку.
POST /api/mailings/{mailing_id}/send/: Обработать активные рассылки и отправить сообщения клиентам.
Статистика
GET /api/statistics/: Получить общую статистику по рассылкам и отправленным сообщениям.

# Stand blog
Новостной блог, написанный на Django. 

## Описание
Данный проект является блогом новостей, разработанным с использованием фреймворка Django. 
Он позволяет пользователям просматривать новости по категорям, тегам и искать определнные посты по названию. Также имеется форма обратной связи.

Шаблон сайта взят templatemo. Проект создан для отображение навыков работы с Django Templates.

## Установка
1. Склонируйте репозиторий: `git clone https://github.com/AngelinaCher/stand-blog.git`
2. Перейдите в директорию проекта `cd stand_blog_site`
3. Создайте виртуальное окружение: `python -m venv venv`
4. Активируйте виртуальное окружение:
   * Для Windows: `venv\Scripts\activate`
   * Для Linux: `source venv/bin/activate`
5. Установите зависимости: `pip install -r requirements.txt`
6. Примените миграции: `python manage.py makemigrations` и `python manage.py migrate`
7. Создайте суперпользователя: `python manage.py createsuperuser`
8. Запустите сервер разработки: `python manage.py runserver`

### Установка с использованием Poetry
1. Склонируйте репозиторий: `git clone https://github.com/AngelinaCher/stand-blog.git`
2. Перейдите в директорию проекта `cd stand_blog_site`
3. Активируйте виртуальное окружение: `poetry shell`
4. Установите зависимости с помощью Poetry: `poetry install`
5. Примените миграции: `python manage.py makemigrations` и `python manage.py migrate`
7. Создайте суперпользователя: `python manage.py createsuperuser`
8. Запустите сервер разработки: `python manage.py runserver`

## Настройка базы данных
По умолчанию Django использует SQLite. В проекте используется PostgreSQL. Для этого нужно изменить данные в settings.py на свои.

## Использование

* Перейдите в браузере по адресу http://localhost:8000/ для просмотра блога
* Для администрирования новостей перейдите по адресу http://localhost:8000/admin/. Используйте данные вашей учетной записи администратора.
Через панель админа можно добавлять и удалять записи.

## Технологии
* Python 3.10.12
* Django 4.2.4
* PostgreSQL
* Bootstrap
* JavaScript

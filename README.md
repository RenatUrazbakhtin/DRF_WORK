# DRF_WORK

## Описание проекта

Проект LMS для работы с курсами и уроками. Реализованна подписка на курс и его оплата с помощью Stripe.

В рамках проекта реализована бэкенд-часть SPA веб-приложения.

## Технологии 

- Python
- Pip
- Django
- DRF
- PostgreSQL
- Redis
- Celery
- Docker
- Docker Compose

## Зависимости

Зависимости расположены в файле requirements.txt. Их установка обеспечивается командой `pip install -r requirements.txt`.

## Файл .env_sample
POSTGRES_DB, POSTGRES_USER, POSTGRES_PASSWORD, POSTGRES_HOST, POSTGRES_PORT - данные для подключения к бд

STRIPE_API - API токен Stripe

EMAIL_HOST_USER, EMAIL_HOST_PASSWORD - данные для отправки сообщений через Yandex

django_secretkey - ключ django

## Работа с проектом

1) Установить на компьютер Docker и Docker Compose с помощью инструкции [https://docs.docker.com/engine/install/](https://docs.docker.com/engine/install/)
2) Клонировать репозиторий себе на компьютер
3) Создать файл .env по примеру .env_sample
4) Собрать Docker образ с помощью команды `docker-compose build`
5) Создайте БД командой `docker-compose exec db psql -U <postgres_user>`, а затем командой `CREATE DATABASE <database_name>;`
6) Запустить контейнер с помощью команды `docker-compose up`

## Документация

- Swagger: `swagger/`
- Redoc: `redoc/`

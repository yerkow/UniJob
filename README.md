<<<<<<< HEAD
# UniJob

**UniJob** — это веб-приложение для поиска работы студентами и упрощения процесса подачи заявок на вакансии.

## Быстрый старт

1. Склонируй репозиторий:
=======
# Быстрый старт

1. Склонируйте репозиторий:
>>>>>>> a6605218752130078d4442fe3fd0996a1dc1289a
   ```bash
   git clone https://github.com/RollSatrs/UniJob.git
   cd UniJob
   ```
<<<<<<< HEAD
2. Создай и активируй виртуальное окружение:
=======
2. Создайте и активируйте виртуальное окружение:
>>>>>>> a6605218752130078d4442fe3fd0996a1dc1289a
   ```bash
   python -m venv venv
   # Для Windows:
   venv\Scripts\activate
   # Для Linux/MacOS:
   source venv/bin/activate
   ```
<<<<<<< HEAD
3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запусти сервер:
=======
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите сервер:
>>>>>>> a6605218752130078d4442fe3fd0996a1dc1289a
   ```bash
   uvicorn backend.routes.api:app --reload --port 8080
   ```

<<<<<<< HEAD
После запуска перейди в браузере по адресу:
[http://localhost:8080/](http://localhost:8080/)

## Технологический стек
- Python (FastAPI, Uvicorn)
- PostgreSQL
- HTML, CSS, JavaScript (frontend в папке syte)

## Структура проекта
- backend — серверный код (роуты, контроллеры, работа с БД)
- syte — фронтенд: страницы, стили, скрипты, изображения

## Переменные окружения
Смотри файл .env.example для примера необходимых переменных.
=======
После запуска перейдите в браузере по адресу:  
[http://localhost:8080/](http://localhost:8080/)
>>>>>>> a6605218752130078d4442fe3fd0996a1dc1289a

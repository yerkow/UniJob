# UniJob

**UniJob** — это веб-приложение для поиска работы студентами и упрощения процесса подачи заявок на вакансии.

## Быстрый старт

1. Склонируй репозиторий:
   ```bash
   git clone https://github.com/RollSatrs/UniJob.git
   cd UniJob
   ```
2. Создай и активируй виртуальное окружение:
   ```bash
   python -m venv venv
   # Для Windows:
   venv\Scripts\activate
   # Для Linux/MacOS:
   source venv/bin/activate
   ```
3. Установи зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запусти сервер:
   ```bash
   uvicorn backend.routes.api:app --reload --port 8080
   ```

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

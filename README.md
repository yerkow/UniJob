# Быстрый старт

1. Склонируйте репозиторий:
   ```bash
   git clone https://github.com/RollSatrs/UniJob.git
   cd UniJob
   ```
2. Создайте и активируйте виртуальное окружение:
   ```bash
   python -m venv venv
   # Для Windows:
   venv\Scripts\activate
   # Для Linux/MacOS:
   source venv/bin/activate
   ```
3. Установите зависимости:
   ```bash
   pip install -r requirements.txt
   ```
4. Запустите сервер:
   ```bash
   uvicorn backend.routes.api:app --reload --port 8080
   ```

После запуска перейдите в браузере по адресу:  
[http://localhost:8080/](http://localhost:8080/)

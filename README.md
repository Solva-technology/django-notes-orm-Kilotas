# Django Notes Project with Docker

## 📌 Описание проекта

Это учебный Django-проект для заметок, развернутый с помощью Docker и PostgreSQL.

Функционал:
- Пользователи с профилем (биография, дата рождения)
- Заметки с текстом, статусом и категориями
- Удобная админка с кастомным интерфейсом
- Локализация и настройка языка/таймзоны через .env
- Docker-окружение для локального запуска

---

## ✅ Используемые технологии

- Django 5
- PostgreSQL
- Docker / Docker Compose
- Python 3.10
- python-dotenv

---

## 🚀 Как запустить проект

### 1️⃣ Клонируй репозиторий

```bash
git clone https://github.com/Solva-technology/django-notes-orm-Kilotas.git
cd django-notes-orm-Kilotas


2️⃣ Создай и заполни .env
В корне проекта создай файл .env. Пример содержимого:

DB_ENGINE=django.db.backends.postgresql
DB_NAME=postgres
DB_USER=postgres
DB_PASSWORD=postgres
DB_HOST=db
DB_PORT=5432
SECRET_KEY=django-insecure-7@h38u$5@x5s8b#e)4q@4$8+72z_6h7jz*e$6)7(k^3+d9x$&z
DJANGO_SECRET_KEY=django-insecure-7@h38u$5@x5s8b#e)4q@4$8+72z_6h7jz*e$6)7(k^3+d9x$&z

DJANGO_LANGUAGE_CODE=ru-ru
DJANGO_TIME_ZONE=UTC

DJANGO_DEBUG=True
DJANGO_ALLOWED_HOSTS=localhost,127.0.0.1


3️⃣ Собери и запусти контейнеры
docker-compose up --build

✅ После этого проект будет доступен на:
http://127.0.0.1:8000/

4️⃣ Применить миграции
docker-compose run web python manage.py migrate


5️⃣ Загрузить фикстуру (если есть)
Если у тебя в корне лежит all_data.json:
docker-compose run web python manage.py loaddata all_data.json


Создать суперпользователя
docker-compose run web python manage.py createsuperuser


7️⃣ Остановить контейнеры
docker-compose down





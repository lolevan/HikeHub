
# HikeHub

HikeHub — это веб-приложение для управления походами и заявками на участие. Проект состоит из двух частей:
- **Публичный сайт (SSR)**: отображает список запланированных походов, позволяет искать по названию, просматривать детали и отправлять заявку с валидацией.
- **Панель управления (SPA)**: предоставляет интерфейс для администраторов для управления походами и заявками, включая регистрацию/вход с JWT‑аутентификацией, CRUD‑операции и изменение статуса заявок.

Проект реализован с использованием:
- **Backend**: Django, Django REST Framework, Celery, Redis, JWT‑аутентификация, Docker
- **Frontend**: Nuxt.js (версии 2) — два приложения: публичный сайт (SSR) и панель управления (SPA)
- **Контейнеризация**: Docker Compose для развертывания всего стека
- **CI/CD**: GitLab CI/CD для автоматической сборки и деплоя

---

## Структура проекта

```
project-root/
├── backend/
│   ├── Dockerfile
│   ├── requirements.txt
│   ├── manage.py
│   ├── config/
│   │   ├── __init__.py
│   │   ├── settings.py
│   │   ├── urls.py
│   │   └── wsgi.py
│   ├── apps/
│   │   ├── hikes/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   └── views.py
│   │   ├── applications/
│   │   │   ├── __init__.py
│   │   │   ├── models.py
│   │   │   ├── serializers.py
│   │   │   ├── tasks.py
│   │   │   └── views.py
│   │   └── users/
│   │       ├── __init__.py
│   │       ├── models.py
│   │       ├── urls.py
│   │       └── views.py
│   └── management/
│       └── commands/
│           ├── __init__.py
│           └── create_fake_data.py
├── frontend/
│   ├── public/              # Публичный сайт (SSR)
│   │   ├── nuxt.config.js
│   │   ├── package.json
│   │   └── pages/
│   │       ├── index.vue    # Список походов
│   │       └── hike/
│   │           └── _id.vue  # Детали похода + форма заявки
│   └── admin/               # Панель управления (SPA)
│       ├── nuxt.config.js
│       ├── package.json
│       ├── middleware/
│       │   └── auth.js
│       ├── store/
│       │   └── index.js
│       └── pages/
│           ├── index.vue        # Главная страница панели
│           ├── login.vue        # Форма входа
│           ├── hikes.vue        # Управление походами
│           ├── hikes/
│           │   └── create.vue   # Создание похода
│           └── applications.vue # Управление заявками
├── docker-compose.yml
├── nginx.conf
├── .env
└── .gitlab-ci.yml
```

---

## Установка и запуск

### Требования

- Docker и Docker Compose  
- (Опционально) Node.js и npm для разработки фронтенд‑приложений локально

### Настройка

1. **Клонируйте репозиторий:**

   ```bash
   git clone https://github.com/lolevan/HikeHub.git
   cd HikeHub
   ```

2. **Настройте файл окружения (.env):**

   Создайте файл `.env` в корне проекта и добавьте переменные (пример ниже):

   ```bash
   DJANGO_SECRET_KEY=your-secret-key
   DEBUG=True
   MYSQL_DATABASE=hikes_db
   MYSQL_USER=user
   MYSQL_PASSWORD=userpassword
   MYSQL_HOST=db
   MYSQL_PORT=3306
   CELERY_BROKER_URL=redis://redis:6379/0
   ```

3. **Запустите проект через Docker Compose:**

   ```bash
   docker-compose up -d
   ```
   временный фикс
   ```bash
   docker-compose exec web python manage.py migrate --noinput
   ```

   При первом запуске будут выполнены:
   - Миграции Django
   - Команда `create_fake_data` (генерация 10 фейковых походов и случайное число заявок) (docker-compose exec web python manage.py create_fake_data) 
   - Запуск gunicorn (Django), Celery‑воркера, Redis, базы данных (MariaDB) и Nginx

4. **Проверьте работу:**

   - Перейдите на [http://localhost](http://localhost) — Nginx проксирует запросы к Django API.
   - Для фронтенд‑приложений (если разворачиваете локально):
     - Публичный сайт (SSR): зайдите в `frontend/public`, выполните `npm install` и `npm run dev`.
     - Панель управления (SPA): зайдите в `frontend/admin`, выполните `npm install` и `npm run dev`.

---

## Функциональность

- **Публичный сайт (Nuxt SSR):**
  - Отображает список походов с поиском по названию (ленивая загрузка изображений).
  - Страница деталей похода с описанием и формой заявки.
  - Форма заявки валидируется на лету (с использованием vee-validate) и отправляется через асинхронный запрос (Celery — задержка 5 секунд).

- **Панель управления (Nuxt SPA):**
  - Авторизация пользователей (JWT‑токен, регистрация, вход).
  - CRUD‑операции для управления походами (создание, редактирование, удаление, загрузка изображений).
  - Отображение заявок в виде таблицы с возможностью пометить заявку как отменённую.

- **Бэкенд:**
  - Django REST Framework предоставляет два API-префикса:
    - `/api/v1/public` — для публичного сайта.
    - `/api/v1/private` — для панели управления (с авторизацией).
  - Celery + Redis используются для асинхронной обработки создания заявок.
  - Команда `create_fake_data` генерирует фейковые данные при первом запуске.

---

## Развертывание и CI/CD

- **Docker Compose**: весь проект можно развернуть одной командой `docker-compose up -d`.
- **GitLab CI/CD**: файл `.gitlab-ci.yml` настроен для автоматической сборки и деплоя Docker-образов.
- **Nginx**: используется в качестве reverse-proxy.

---

## Разработка

- Для разработки бэкенда:  
  Запускайте `python manage.py runserver` внутри контейнера или локально, если настроено виртуальное окружение.

- Для разработки фронтенд‑приложений:  
  В папках `frontend/public` и `frontend/admin` выполните `npm install` и `npm run dev`.

---

## Лицензия

Проект распространяется под лицензией MIT. Подробнее см. в файле [LICENSE](LICENSE).

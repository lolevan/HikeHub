FROM python:3.9-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

WORKDIR /app

COPY requirements.txt /app/
RUN pip install --upgrade pip && pip install -r requirements.txt

COPY . /app/

# При запуске: миграции + фейковые данные + gunicorn
CMD ["sh", "-c", "python manage.py migrate && python manage.py create_fake_data && gunicorn config.wsgi:application --bind 0.0.0.0:8000"]

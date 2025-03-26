#!/bin/sh
set -e

echo "Ожидаем доступности базы данных $MYSQL_HOST:$MYSQL_PORT..."
while ! mysqladmin ping -h"$MYSQL_HOST" -P"$MYSQL_PORT" -u"$MYSQL_USER" -p"$MYSQL_PASSWORD" --silent; do
  echo "База данных не готова, ждем..."
  sleep 1
done

echo "База данных доступна. Ждем дополнительные 5 секунд..."
sleep 5

echo "Создаем миграции для кастомных приложений..."
python manage.py makemigrations

echo "Запускаем миграции..."
python manage.py migrate --noinput

echo "Создаем фейковые данные (если их еще нет)..."
python manage.py create_fake_data

echo "Запускаем Gunicorn..."
exec gunicorn config.wsgi:application --bind 0.0.0.0:8000

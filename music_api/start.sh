gunicorn music_api.wsgi:application
python manage.py collectstatic --noinput
python manage.py runserver 0.0.0.0:$PORT
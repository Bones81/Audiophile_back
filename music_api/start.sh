gunicorn music_api.wsgi
python manage.py runserver 0.0.0.0:$PORT
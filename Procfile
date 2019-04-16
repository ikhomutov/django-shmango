release: django-admin migrate --noinput
release: django-admin collectstatic --noinput
web: gunicorn shmango.wsgi:application

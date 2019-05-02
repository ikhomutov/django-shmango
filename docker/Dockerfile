FROM python:3.6

WORKDIR /app
COPY requirements /app/requirements

ENV PYTHONPATH "${PYTONPATH}:/app"
ENV PYTHONUNBUFFERED 1

RUN pip install -r requirements/prod.txt

COPY ./ /app

RUN django-admin collectstatic --noinput --settings shmango.settings.base

EXPOSE 8000

CMD ["gunicorn", "-c", "/app/docker/configs/gunicorn.conf", "shmango.wsgi:application"]

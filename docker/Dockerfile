FROM python:3.6

WORKDIR /app
COPY ./ /app

RUN pip install -r requirements/prod.txt

ENV PYTHONPATH '${PYTONPATH}:/app'
ENV PYTHONUNBUFFERED 1

EXPOSE 8000

CMD ['gunicorn','-c', '/app/docker/configs/gunicorn.conf', 'shmango.wsgi:application']

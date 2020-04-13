FROM python:3

ENV PYTHONUNBUFFERED 1

RUN mkdir /code
WORKDIR /code
COPY requirements.txt /code/
RUN pip install -r requirements.txt
COPY . /code/

CMD uwsgi --chdir=/code \
    --module=project.wsgi:application \
    --env DJANGO_SETTINGS_MODULE=project.settings \
    --master --pidfile=/tmp/project-master.pid \
    --http=0.0.0.0:8000 \
    --processes=5 \
    --uid=1000 --gid=2000 \
    --harakiri=20 \
    --max-requests=5000 \
    --vacuum \
    --check-static /code
    #--daemonize=/var/log/uwsgi/yourproject.log      # background the process

FROM python:3.7-alpine

RUN adduser -D flask

WORKDIR /home/flask

COPY launch/requirements.txt requirements.txt
RUN python -m venv venv
RUN venv/bin/pip install --no-cache-dir -r requirements.txt
RUN venv/bin/pip install gunicorn

COPY launch/app app
COPY launch/launch.py launch/config.py launch/boot.sh ./
RUN chmod +x boot.sh

ENV FLASK_APP launch.py

RUN chown -R flask:flask ./
USER flask

EXPOSE 5000
ENTRYPOINT ["./boot.sh"]

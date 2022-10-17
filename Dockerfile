FROM python:3.10.7

WORKDIR /app

COPY requirements.txt requirements.txt

COPY . .

RUN pip3 install -r requirements.txt

EXPOSE 8003

CMD python manage.py collectstatic
CMD gunicorn --bind 0.0.0.0:8003 django_calculator.wsgi
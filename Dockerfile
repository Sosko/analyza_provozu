FROM python:3.11.2-alpine3.17
WORKDIR /var/www
RUN pip install django django-cors-headers 
RUN apk add postgresql gcc && pip install psycopg2-binary
CMD ["python", "manage.py", "runserver"]
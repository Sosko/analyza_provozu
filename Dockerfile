FROM python:3.11.2-alpine3.17
RUN pip install django
WORKDIR /var/www
CMD ["python", "manage.py", "runserver"]


FROM    python:3.13

RUN     git clone  https://github.com/Nipun-Chaudhari/django_learn.git

WORKDIR django_learn/learn_models/

RUN     pip install django

CMD     ["python", "manage.py", "makemigrations"]

CMD     ["python", "manage.py", "migrate"]

EXPOSE  8000

CMD     ["python", "manage.py", "runserver", "0.0.0.0:8000"]
~                                                             

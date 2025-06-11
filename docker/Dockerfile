FROM python:3.13

ENV DockerHOME=/home/app/drf_api

RUN	apt-get install -y git && \
	 git clone https://github.com/Nipun-Chaudhari/django_learn.git

WORKDIR  /django_learn/learn_models/

RUN 	pip install django 

CMD 	["python3" ,"manage.py" ,"makemigrations"]

CMD 	["python3" , "manage.py" ,"migrate"]

CMD	["pyhton3" , "manage.py" , "runserver" ]

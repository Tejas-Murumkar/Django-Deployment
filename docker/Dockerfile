FROM python:3.13

ENV APP_HOME=/home/app/web

# Install OS packages
RUN apt-get update && apt-get install -y git

# Clone Django project (if truly needed)
RUN git clone https://github.com/Tejas-Murumkar/Django-Deployment.git
WORKDIR Django-Deployment/django_learn/learn_models/

# Install dependencies (replace this with requirements.txt ideally)
RUN pip install django

# Expose port
EXPOSE 8000

# Start Django app
CMD ["sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]


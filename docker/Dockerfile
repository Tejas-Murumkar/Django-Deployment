FROM ubuntu:latest

RUN apt update -y && \
    apt upgrade -y && \
    apt install -y git nginx python3 python3-pip python3-django

# Clone the Django project
RUN git clone https://github.com/Nipun-Chaudhari/django_learn.git

WORKDIR /django_learn/learn_models/

# Copy custom Nginx config if needed
COPY nginx.conf /etc/nginx/nginx.conf

# Expose Django default port
EXPOSE 8000

# Run all commands in one shell execution
CMD bash -c "\
    python3 manage.py makemigrations && \
    python3 manage.py migrate && \
    python3 manage.py runserver "


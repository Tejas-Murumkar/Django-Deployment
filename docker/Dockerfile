FROM python:3.13

ENV APP_HOME=/home/app/web
WORKDIR $APP_HOME

# Install system dependencies
RUN apt-get update

# Copy project files
COPY learn_models/ ./learn_models/

WORKDIR /learn_models/

# Install Python dependencies
RUN pip install django

# Expose port
EXPOSE 8000

# Start Django app
CMD ["sh", "-c", "python3 manage.py makemigrations && python3 manage.py migrate && python3 manage.py runserver 0.0.0.0:8000"]


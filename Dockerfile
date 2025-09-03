FROM python:3.11-slim

WORKDIR /app

COPY requirements.txt /tmp/requirements.txt

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    pip install --upgrade pip && \
    pip install -r /tmp/requirements.txt && \
    rm -rf /var/lib/apt/lists/*

COPY . /app

EXPOSE 8000

RUN useradd -m django-user
USER django-user

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]

FROM python:3.11-slim

RUN apt-get update && apt-get install -y \
    libpq-dev gcc && \
    rm -rf /var/lib/apt/lists/*
WORKDIR /core
COPY requirements.txt /core/

RUN python -m pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . /core/

EXPOSE 8000

CMD ["sh", "-c","gunicorn", "seu_projeto.wsgi:application", "python manage.py migrate && python manage.py runserver 0.0.0.0:8000"]

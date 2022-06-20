# syntax=docker/dockerfile:1

FROM python:3.10-slim-buster

WORKDIR /app

COPY requirements.txt requirements.txt

RUN pip3 install -r requirements.txt

COPY web_numbers/orders ./orders

ENV PYTHONPATH "${PYTHONPATH}:/app/orders/bot"

CMD ["python3.10", "orders/bot/app.py", "--host=0.0.0.0"]
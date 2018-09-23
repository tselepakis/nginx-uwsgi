FROM python:3.7-alpine

WORKDIR /app

RUN apk add --no-cache \
    gcc \
    libc-dev \
    linux-headers

COPY requirements.txt /app/requirements.txt
RUN  pip install --no-cache-dir -r /app/requirements.txt

COPY . /app

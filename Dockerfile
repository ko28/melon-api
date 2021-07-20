# syntax=docker/dockerfile:1
FROM python:3.8-slim-buster

COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt

WORKDIR /app

COPY melonapi/ .

CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]

FROM python:3.8.11-buster

RUN apt-get update && apt-get install postgresql-client -y

RUN mkdir /code

WORKDIR /code

COPY requirements.txt /code/

RUN pip install -r requirements.txt

COPY .. /code/

EXPOSE 8000
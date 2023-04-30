FROM python:3.10.6-slim-buster

ENV PYTHONUNBUFFERED 1
RUN mkdir /retailys
WORKDIR /retailys
COPY . /retailys/
RUN pip install -r requirements.txt


FROM python:3.10.14-slim

ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

RUN mkdir /proto_dmd
WORKDIR /proto_dmd

COPY requirements.txt /proto_dmd/

RUN pip install --upgrade pip
RUN pip install -r requirements.txt

COPY . /proto_dmd/

# pull official base image
FROM python:3.10-slim-buster

# creates a new user named admin
RUN adduser --disabled-password eco_admin

# set working directory
WORKDIR /ecoback

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# install system dependencies
RUN apt-get update \
  && apt-get -y install netcat gcc postgresql python-psycopg2 libpq-dev\
  && apt-get clean

# install dependencies
COPY ./requirements.txt .
RUN pip install -U setuptools
RUN pip install --upgrade pip
RUN pip install -r requirements.txt

# add app
COPY . .

# run server
RUN ["chmod", "+x", "/ecoback/entrypoint.sh"]

# change owner
RUN chown -R eco_admin:eco_admin ./
USER eco_admin
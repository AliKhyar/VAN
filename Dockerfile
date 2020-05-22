# import the base image
FROM python:3.7

#set  the env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
    #django env vars
ENV DJANGO_SECRET_KEY ws7$$2*^-nn)f7o4u!b83i+5zv@c^x%7q2^x-k+a=3^&ft))#q$$
ENV DEBUG True
# set the workdir

WORKDIR /code

#install dependencies
COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

#copy the project

COPY . /code/

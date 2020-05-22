# import the base image
FROM python:3.7

#set  the env variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
    #django env vars
#ENV DJANGO_SECRET_KEY -wxdxfjbkyq00rg2g*)%el#psremzta#cz2xt5u0q7z+161txj
# set the workdir

WORKDIR /code

#install dependencies
COPY Pipfile Pipfile.lock /code/

RUN pip install pipenv && pipenv install --system

#copy the project

COPY . /code/

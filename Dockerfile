FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /mathematics

RUN apt-get update \
    && apt-get install aspell -y

COPY . .

RUN pipenv install --system

FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /mathematics

RUN apt-get update \
    && apt-get install aspell -y

COPY . .

RUN pipenv sync

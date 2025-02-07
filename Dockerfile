FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /mathematics

RUN export DEBIAN_FRONTEND=noninteractive
RUN apt-get update \
    && apt-get install -y aspell

COPY . .

RUN pipenv install --system --deploy

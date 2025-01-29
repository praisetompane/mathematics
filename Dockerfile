FROM mcr.microsoft.com/devcontainers/python:3.12

WORKDIR /mathematics

COPY . .

RUN pipenv install

FROM mcr.microsoft.com/devcontainers/python:3.13

WORKDIR /mathematics

COPY . .

RUN apt-get update

RUN apt-get install aspell -y

RUN pipenv sync --system -d

RUN adduser -u 5678 --disabled-password --gecos "" mathematics && chown -R mathematics /mathematics
USER mathematics
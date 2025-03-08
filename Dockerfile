FROM mcr.microsoft.com/devcontainers/python:3.11

WORKDIR /mathematics

RUN apt-get update \
    && apt-get install aspell -y

COPY . .

RUN pipenv sync --system -d

RUN adduser -u 5678 --disabled-password --gecos "" mathematics && chown -R mathematics /mathematics
USER mathematics
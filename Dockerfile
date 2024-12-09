FROM mcr.microsoft.com/devcontainers/python:1-3.12-bullseye

USER vscode 

WORKDIR /mathematics

RUN export DEBIAN_FRONTEND=noninteractive
RUN sudo apt-get update
RUN sudo apt-get clean
RUN sudo rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt

RUN pip install --cache-dir /pip.cache --src /usr/local/src -r requirements.txt

RUN sudo curl -O https://raw.githubusercontent.com/praisetompane/machine_setup/refs/heads/main/git_facade.sh

RUN sudo chmod +x ./git_facade.sh

RUN ./git_facade.sh
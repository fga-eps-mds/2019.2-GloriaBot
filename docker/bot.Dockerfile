FROM python:3.6

RUN apt update && apt install -y git

RUN python pip install --upgrade pip

ADD ./requirements.txt /tmp

ADD ./bot /bot

WORKDIR /bot


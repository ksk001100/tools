FROM python:3.8.4-buster
USER root

ENV DEBCONF_NOWARNINGS yes

RUN apt-get update && apt-get upgrade -y && apt-get install -y vim tor
RUN pip install --upgrade pip
RUN pip install PySocks

WORKDIR /workspace

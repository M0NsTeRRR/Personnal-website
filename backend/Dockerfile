FROM python:3.7-alpine

LABEL maintainer="Ludovic Ortega mastership@hotmail.fr"

# update package
RUN apk update

# copy program and requirements
COPY * /app/backend/

# install dependencies
RUN pip3 install -r /app/backend/requirements.txt

# install gunicorn
RUN pip3 install gunicorn

# set workdir
WORKDIR /app/backend/

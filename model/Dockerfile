FROM python:3.7.7-slim-buster

RUN apt-get update && apt-get -y install \
    gcc

RUN pip install --upgrade pip

COPY . /workspace
WORKDIR /workspace
RUN chmod +x docker-entrypoint.sh
RUN pip install -r requirements.txt

EXPOSE 8888

ENTRYPOINT ["/workspace/docker-entrypoint.sh"]

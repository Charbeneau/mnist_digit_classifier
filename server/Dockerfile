FROM python:3.7.7-slim-buster

RUN apt-get update && apt-get -y install \
    gcc \
    libgtk2.0-dev

RUN pip install --upgrade pip

COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENTRYPOINT ["python"]
CMD ["app.py"]

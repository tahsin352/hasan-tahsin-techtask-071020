FROM python:3.8
MAINTANER Tahsin Hasan "tahsin352@yahoo.com"
ENV FLASK_APP "app.py"
ENV FLASK_ENV "production"

RUN mkdir /app
WORKDIR /app

COPY Pip* /app/

RUN pip install --upgrade pip && \
    pip install pipenv && \
    pipenv install --dev --system --deploy --ignore-pipfile

ADD . /app

EXPOSE 5000

CMD flask run --host=0.0.0.0
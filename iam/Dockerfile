# Use a suitable base image

FROM --platform=$BUILDPLATFORM python:3.10-slim-bookworm AS builder

WORKDIR /app

# Update the package list and install packages
RUN apt-get update

COPY requirements.txt /app/
RUN pip install -r requirements.txt
RUN pip install gunicorn

RUN mkdir -p /app/staticfiles
COPY . /app/
RUN python manage.py migrate
RUN python manage.py collectstatic --noinput

CMD ["gunicorn", "iam.wsgi"]
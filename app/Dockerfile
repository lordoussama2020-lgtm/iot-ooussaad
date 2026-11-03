FROM python:3.12-alpine

WORKDIR /app

COPY app.py .

ARG APP_VERSION=v1
ENV APP_VERSION=${APP_VERSION}

EXPOSE 8888

CMD ["python", "app.py"]

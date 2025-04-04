FROM alpine:3.13

RUN apk add --no-cache py3-pip python3 && \
    pip3 install flask requests Flask-Opentracing jaeger-client prometheus-client opentracing

COPY . /usr/src/myapp

ENV FLASK_APP test-app.py

WORKDIR /usr/src/myapp

EXPOSE 8000

CMD flask run --host=0.0.0.0 --port=8000

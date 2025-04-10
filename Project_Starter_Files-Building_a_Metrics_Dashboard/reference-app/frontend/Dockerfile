# Use the official Python image.
# https://hub.docker.com/_/python
FROM python:3.13-slim

# Copy local code to the container image.
WORKDIR /app
COPY . ./

# Install production dependencies.
RUN apt-get update && \
    pip install --upgrade pip && \
    pip install -r requirements.txt

CMD ["gunicorn", "--access-logfile", "-", "--error-logfile", "-", "-w", "4", "-b", "0.0.0.0:8080", "app:app"]

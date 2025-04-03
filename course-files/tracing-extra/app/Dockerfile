# Use the official lightweight Python image.
# https://hub.docker.com/_/python
FROM python:3.13-slim

# Copy local code to the container image.
ENV APP_HOME /app
WORKDIR $APP_HOME
COPY . ./

# Install production dependencies.
RUN pip install -r requirements_3.9.txt
# Install dependecies without installing package depencies to avoid conflicts
RUN pip install --no-deps redis-opentracing

RUN pip freeze

# Set environment variables for Flask
ENV FLASK_APP=app.py  
ENV FLASK_RUN_HOST=0.0.0.0 
ENV FLASK_RUN_PORT=7111  

# Expose the port Flask will run on
EXPOSE 7111

# Run Flask directly
CMD ["flask", "run"]

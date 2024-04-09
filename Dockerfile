FROM python:3.9-slim

RUN apt-get update \
  # dependencies for building Python packages \
  && apt-get install -y build-essential \
  # psycopg2 dependencies
  && apt-get install -y libpq-dev \
  # Translations dependencies
  && apt-get install -y gettext \
  # Nginx
  && apt-get install nginx vim procps curl libpq-dev -y --no-install-recommends \
  # cleaning up unused files
  && apt-get purge -y --auto-remove -o APT::AutoRemove::RecommendsImportant=false \
  && rm -rf /var/lib/apt/lists/*

COPY agent/nginx.default /etc/nginx/sites-available/default
RUN ln -sf /dev/stdout /var/log/nginx/access.log \
    && ln -sf /dev/stderr /var/log/nginx/error.log

# Set environment variables
ENV PIP_DISABLE_PIP_VERSION_CHECK 1
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /code

# Copy project
COPY ./agent .
RUN chown -R www-data:www-data /code

# Install dependenciess
COPY agent/requirements.txt .
RUN pip install -r requirements.txt

COPY agent/start-server.sh .
RUN sed -i 's/\r$//g' start-server.sh
RUN chmod +x start-server.sh

EXPOSE 8080
STOPSIGNAL SIGTERM
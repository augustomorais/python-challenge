# PostgreSQL Docker Setup

This project provides a Docker setup for running a PostgreSQL database. It includes a `docker-compose.yml` file and an optional `Dockerfile` for custom configurations.

## Dockerfile

The `Dockerfile` is used to build a custom PostgreSQL image. This step is optional as you can use the official PostgreSQL image directly. If customization is needed, use the following template:

```Dockerfile
# Use the official PostgreSQL image as a base
FROM postgres:latest

# Set environment variables
ENV POSTGRES_DB=mydatabase
ENV POSTGRES_USER=myuser
ENV POSTGRES_PASSWORD=mypassword

# Add initialization scripts if needed
COPY ./init.sql /docker-entrypoint-initdb.d/


# Setup
docker-compose up --buid
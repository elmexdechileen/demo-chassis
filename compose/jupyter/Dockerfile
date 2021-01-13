FROM jupyter/datascience-notebook


USER root
RUN apt-get update && \
    apt-get install -y --no-install-recommends \
    redis-tools && \
    apt-get clean && rm -rf /var/lib/apt/lists/*

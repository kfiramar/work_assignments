FROM ubuntu:latest
ENV VERSION=1.2.0
RUN apt-get update && apt-get install -y python vim zip unzip \
    && rm -rf /var/lib/apt/lists/*
RUN useradd -m myuser
USER myuser
COPY --chown=myuser:myuser zip_job.py /tmp/zip_job.py
CMD uname -a && [ -f /tmp/zip_job.py ] && echo "/tmp/zip_job.py exists" || exit 1

FROM gcr.io/google.com/cloudsdktool/cloud-sdk:latest

COPY requirements.txt /tmp/
VOLUME /data

RUN pip install --no-cache-dir -r /tmp/requirements.txt && \
  curl -L https://github.com/wercker/stern/releases/download/1.11.0/stern_linux_amd64 -o /usr/local/bin/stern && \
  chmod 755 /usr/local/bin/stern

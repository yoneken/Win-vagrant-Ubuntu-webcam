FROM ubuntu:18.04
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list && \
    apt update && \
    apt install -y python3-opencv && \
    apt clean && \
    rm -r /var/lib/apt/lists/*

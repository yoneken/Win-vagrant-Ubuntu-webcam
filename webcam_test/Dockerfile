FROM ubuntu:18.04
ENV DEBIAN_FRONTEND=noninteractive
RUN sed -i 's@archive.ubuntu.com@ftp.jaist.ac.jp/pub/Linux@g' /etc/apt/sources.list && \
    apt update && \
    apt install -y python3-opencv python3-pip ffmpeg && \
    pip3 install sk-video argparse && \
    apt clean && \
    rm -r /var/lib/apt/lists/*

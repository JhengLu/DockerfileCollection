# Use the official Ubuntu 22.04 image as a base
FROM ubuntu:22.04

# Set a non-interactive shell to avoid stuck prompts during build
ENV DEBIAN_FRONTEND=noninteractive

# Update the system and install necessary packages, then clean up cache
RUN apt-get update && \
    apt-get upgrade -y && \
    apt-get install -y \
        build-essential \
        autoconf \
        automake \
        libpcre3-dev \
        libevent-dev \
        pkg-config \
        zlib1g-dev \
        libssl-dev \
        vim \
        numactl \
        mpich \
        libtool \
        git && \
    rm -rf /var/lib/apt/lists/*

# Your additional instructions here

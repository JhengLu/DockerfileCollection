'''
docker build -t ubuntu-22.04 .
docker run --gpus all --privileged -it -v /data:/code ubuntu-22.04:latest /bin/bash
'''

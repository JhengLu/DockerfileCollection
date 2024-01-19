#!/bin/bash

while true
do
    numastat -p redis
    sleep 1  # Adjust the sleep duration as needed
done

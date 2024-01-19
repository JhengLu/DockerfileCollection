#!/bin/bash

while true
do
    numastat -p <PID_of_Redis_process>
    sleep 1  # Adjust the sleep duration as needed
done

#!/bin/bash

cd /home

for NETID in $(ls -d *); do
  JOBS=$(sacct -u $NETID -S 05/14/20 -E 10/30/20 -n -r gpu --format=jobid,partition | wc -l)
  echo $NETID $JOBS >> /home/jdh4/software/gpu_users/check.txt
  #echo $NETID $JOBS
  #sleep 1
done

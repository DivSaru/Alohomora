#!/bin/sh

# Server-side script

# Starting spark services

# Starting master

$SPARK_HOME/sbin/start-master.sh

# Starting slave or worker

$SPARK_HOME/sbin/start-slave.sh spark://nikita-Lenovo-Z51-70:7077

# Checking for input from client and then performing the necessary actions

x=1

# Always True

while [ $x -eq 1 ]
do

  # shell.sh running infinite times
  sh ./shell.sh
done

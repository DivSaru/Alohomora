#!/bin/sh

# running the camera script and the sensor script in parallel

#cd /home/pi/classifier

python camera.py & python sensor1.py


# Script for checking whether any image is received from client.

# If an image is received from client, pass that image to the image classifier to make the predictions.

# Once predictions are made, send them back to client. 

#!/bin/sh

FILE=""

# Directory path where the image from the client will be received.

DIR="/home/nikita/Desktop/tf_files/images"

# Checking for content in the directory. If the directory is empty, display "empty".. else perform the image classification.

if [ "$(ls -A $DIR)" ]:
then
  
  # Submitting the image classification job to Spark and then generate the labels..

  $SPARK_HOME/bin/spark-submit /home/nikita/Desktop/tf_files/spark_prediction_1.py
  
  # Transfer the predictions made for the image to the client. Here, pi@192.168.43.247 is the client

  scp /home/nikita/Desktop/tf_files/sample.txt pi@192.168.43.247:/home/pi/classifier/
  
  # Empty the directory where the image from the client is received.

  rm /home/nikita/Desktop/tf_files/images/img.jpg
  
  # Delete the contents of the file sample.txt where the predictions are saved.

  truncate -s0 /home/nikita/Desktop/tf_files/sample.txt

else
  echo "Empty"
fi

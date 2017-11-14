

ALOHOMORA (Object Identification and Navigation System) uses model that is built using transfer learning from Google`s deep learning model Inception v3 which is internally trained by Google Inc . on 1000 categories supplied by the ImageNet (2012) with 79.3% confidence .

After training that model again with 10 GB of data using Transfer Learning and Apache Spark as training platform ; applying Tensorflow to classify images which must be send by our device Raspberry Pie (which is further integrated with Camera , Sensor , Speaker and Buzzer ) . Standard output here in the form of Voice(speech)
So basically our input image is classified by our model to produce speech (voice) with 85 % confidence over 75.3% confidence of Google`s ImageNet

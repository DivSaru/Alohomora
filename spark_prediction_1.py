# Tensorflow on Spark

# Image classifier script for making the predictions.

# Makes use of the retrained graph and the retrained labels to make the predictions.

# import the required libraries

import tensorflow as tf
import sys
from pyspark import SparkContext, SparkConf

# creating spark context

conf = SparkConf().setAppName("t1").setMaster("local")
sc=SparkContext(conf=conf)

# Function to perform classification. Takes as input a single image received from client.

def object_classifier():
    
    # The path of the image received from client.

    image_path = "/home/nikita/Desktop/tf_files/images/img.jpg"
    
    # Read in the image_data

    image_data = tf.gfile.FastGFile(image_path, 'rb').read()

    # Loads label file, strips off carriage return

    label_lines = [line.rstrip() for line 
                   in tf.gfile.GFile("/home/nikita/Desktop/tf_files/retrained_labels.txt")]
    
    # Unpersists graph from file

    with tf.gfile.FastGFile("/home/nikita/Desktop/tf_files/retrained_graph.pb", 'rb') as f:
        graph_def = tf.GraphDef()
        graph_def.ParseFromString(f.read())
        _ = tf.import_graph_def(graph_def, name='')

    with tf.Session() as sess:
        # Feed the image_data as input to the graph and get first prediction
        softmax_tensor = sess.graph.get_tensor_by_name('final_result:0')
    
        predictions = sess.run(softmax_tensor, \
             {'DecodeJpeg/contents:0': image_data})
    
        # Sort to show labels of first prediction in order of confidence
        top_k = predictions[0].argsort()[-len(predictions[0]):][::-1]
    
    # Open a file sample.txt in append mode to write the labels generated for the image.

    outputFile = open("/home/nikita/Desktop/tf_files/sample.txt","a")
    
    # Display the predictions made and wrie them to sample.txt file.

    for node_id in top_k:
        human_string = label_lines[node_id]
        score = predictions[0][node_id]
        print('%s (score = %.5f)' % (human_string, score))
        outputFile.write(human_string)
        outputFile.write("\n")

    # Close the sample.txt file.
   
    outputFile.close()

    return


# Store the value of the function in f1 object.

f1 = object_classifier()

# Broadcast the value of f1 object.

f1_bc = sc.broadcast(f1)

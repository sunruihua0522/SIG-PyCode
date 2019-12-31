import tensorflow as tf
import numpy as np
'''
from tensorflow.examples.tutorials.mnist import input_data

mnist=input_data.read_data_sets('MNIST_data', one_hot=True)

x = tf.compat.v1.placeholder('float',shape=[None, 784])
#y = tf.placeholder('float', shape=[None, 10])

w = tf.Variable(tf.zeros([784,10]))
b = tf.Variable(tf.zeros([10]))

y = tf.nn.softmax(tf.matmul(x,w) + b)

y_ = tf.compat.v1.placeholder("float", [None,10])
cross_entropy = -tf.reduce_sum(y_*tf.math.log(y))
train_step = tf.compat.v1.train.GradientDescentOptimizer(0.01).minimize(cross_entropy)
init = tf.compat.v1.global_variables_initializer()
sess = tf.compat.v1.Session()
sess.run(init)

for i in range(500):
    batch_xs, batch_ys = mnist.train.next_batch(100)
    sess.run(train_step, feed_dict={x: batch_xs, y_: batch_ys})

correct_prediction = tf.equal(tf.argmax(y, 1), tf.argmax(y_, 1))
accuracy = tf.reduce_mean(tf.cast(correct_prediction, "float"))
print(sess.run(accuracy, feed_dict={x: mnist.test.images, y_: mnist.test.labels}))
'''

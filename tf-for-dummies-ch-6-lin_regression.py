''' Demonstrates linear regression with TensorFlow '''

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import tensorflow as tf

# Random input values
N = 40
x = tf.random.normal([N])
m_real = tf.random.truncated_normal([N], mean=2.0)
b_real = tf.random.truncated_normal([N], mean=3.0)
y = m_real * x + b_real

# Variables
m = tf.Variable(tf.random.normal([]))
b = tf.Variable(tf.random.normal([]))

# Compute model and loss
model = tf.add(tf.multiply(x, m), b)
loss = tf.reduce_mean(tf.pow(model - y, 2))

# Create optimizer
learn_rate = 0.1
num_epochs = 200
num_batches = N
optimizer = tf.optimizers.SGD(learn_rate).minimize(loss)

# Initialize variables
init = tf.global_variables_initializer()

# Now that the computation is defined we launch a TensorFlow session
with tf.Session() as sess:
    sess.run(init)

    # Perform training
    for epoch in range(num_epochs):
        for batch in range(num_batches):
            sess.run(optimizer)

    # Display results
    print('m = ', sess.run(m))
    print('b = ', sess.run(b))


''' This module sets the number of batches equal to the number of input points. The
training process executes 200 epochs, and each epoch performs 40 training steps.

Any computation in TensorFlow needs to be defined in the context of a graph. In the examples above we did not notice the presence of a graph because the tf.add() statements were implicitly using the default graph. Accordingly the session created by tf.Session() was associated with the default graph. A graph in the TensorFlow sense defines the set of computations which can be performed by a TensorFlow program. The term is misleading insofar as a TensorFlow graph may actually be a collection of disjoint graphs which can be executed independently.
 '''


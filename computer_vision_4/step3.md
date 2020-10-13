Let's now learn about the LearningRateScheduler Callback

## LearningRateScheduler Callback
Every optimizer (that we set in the compile method) has a learning rate argument. Though it takes a default value, it is a parameter that requires tuning - a value too low will take a long time (more epochs) to reach a good accuracy and a value to high will overshoot the minimum and just oscillate at poor values of accuracy. Either way, one way to work with the learning rate is to fix it to a medium-high value and then reduce it on every epoch - resulting in large steps towards the minimum in the start but much slower steps after a while.

We can accomplish this using the LearningRateScheduler. Let's see how!

Create a new file where our code will reside:

```
touch step3.py
```{{execute}}

Opening the file that we just created `step3.py`{{open}}.

We will be using the same Fashion MNIST dataset. Append all the following code, which will import the libraries, clean the data for training and create the model. Don't worry about the two function we are importing, we just want to be able to quickly clean the data and obtain the model.

<pre class="file" data-filename="step1.py" data-target="append">

import tensorflow as tf

# Function to clean up the data
from preprocess_data import prepare_data

#Function to create the model
from model import create_model

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = prepare_data(training_images)
test_images = prepare_data(test_images)

model = create_model()

print(model.summary())

</pre>

Let us now define the callback to include it when we are going to fit the model.

<pre class="file" data-filename="step1.py" data-target="append">

# Scheduler function that reduces the learning rate by a factor of e^-0.1.
def scheduler(epoch, lr):
    if epoch < 5:
        return lr
    else:
        return lr * tf.math.exp(-0.1)

callback2 = tf.keras.callbacks.LearningRateScheduler(scheduler=scheduler,verbose=1)

</pre>

Arguments:
`scheduler`: A function that takes an epoch index (integer, indexed from 0) and current learning rate (float) as inputs and returns a new learning rate as output (float).
`verbose`: int. 0: quiet, 1: update messages.

With our callback defined, we will now move on to compiling and fitting our model.
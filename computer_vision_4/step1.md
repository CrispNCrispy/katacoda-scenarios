In the last scenario, we saw how to create, train and evaluate a convolution neural network. In this scenario we will focus on addiitonal tools that are commonly used to help achieve better results, particularly - Callbacks.

## Creation of a python file with functions to clean the data and create a model
Let us create a python file which will contain the functions to clean our train/test images and create a model so that we can use it directly in the subsequent steps.

```
touch preparation.py
```{{execute}}

<pre class="file" data-filename="preparation.py" data-target="append">

def create_model():
	model = tf.keras.Sequential([
    		tf.keras.layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(32,32,1)),
    		tf.keras.layers.AveragePooling2D(),
    		tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'),
    		tf.keras.layers.AveragePooling2D(),
    		tf.keras.layers.Flatten(),
    		tf.keras.layers.Dense(units=120, activation='relu'),
    		tf.keras.layers.Dense(units=84, activation='relu'),
    		tf.keras.layers.Dense(units=10, activation='softmax')
		])
	return model
	
def prepare_data(images):
	# Normalize the image pixels
	images  = images / 255.0
	# Add an extra dimension to the matrix
	images = np.expand_dims(images,-1)
	# Pad the images to get it into 32x32 size
	images = np.pad(images, ((0,0),(2,2),(2,2),(0,0)), 'constant')
	return images

</pre>

## EarlyStopping Callback
What happens if we run too many epochs? Chances are that the model 'overfits' on the training data, meaning that it fits 'too perfectly' on the training data that it starts performing worse on the test data. We want to avoid this. Wouldn't it be great if we could stop the training when we reach a max accuracy (or any other valuable metric).

For example, if we are monitoring accuracy, we should be able to stop the training if our model's accuracy has stopped improving in `n` consecutive epochs. Luckily, we can do that using the Early Stopping Callback!

Create a new file where our code will reside:

```
touch step1.py
```{{execute}}

Opening the file that we just created `step1.py`{{open}}.

We will be using the same Fashion MNIST dataset. Append all the following code, which will import the libraries, clean the data for training and create the model.

<pre class="file" data-filename="step1.py" data-target="append">

import tensorflow as tf
import matplotlib.pyplot as plt

# Function to clean up the data and create the model
from preparation import prepare_data, create_model

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()

training_images = prepare_data(training_images)
test_images = prepare_data(test_images)

model = create_model()

print(model.summary())

</pre>

Let us now define the callback to include it when we are going to fit the model.

<pre class="file" data-filename="step1.py" data-target="append">

callback1 = tf.keras.callbacks.EarlyStopping(
                    monitor='val_accuracy',
                    mode='max', min_delta=0.001,
                    patience = 2)

</pre>

Arguments:
`monitor`: Passing `accuracy` to be monitored in the EarlyStopping callback instance.

`mode` : `max` as we aim for max accuracy. For `loss` it would have been `min`.

`min_delta = 0.001`: 	Minimum change in the monitored quantity to qualify as an improvement, i.e. an absolute change of less than min_delta, will count as no improvement.

`patience`: Number of epochs with no improvement after which training will be stopped.

With our callback defined, we will now move on to compiling and fitting our model.
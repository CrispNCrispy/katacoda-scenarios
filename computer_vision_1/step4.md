
It always takes a bit of time to reach the desired level of accuracy for a model. We have to keep experimenting with the number of epochs we should train the model for.

Wouldn't it be great if we could stop the training when we reach a max accuracy(or any other valuable metric)?
For example, is we are monitoring accuracy, we should be able to stop the training if our model's accuracy has stopped improving in `n` consecutive epochs. Luckily, we can do that using Callbacks!

Let's quickly create a new file:
```
touch step4.py
```{{execute}}

Open the file `step4.py`{{open}}.

Import tensorflow and add the following steps to prepare fashion mnist data for training and testing as done in step 2

<pre class="file" data-filename="step4.py" data-target="append">

import tensorflow as tf
print(tf.__version__)

# using the same dataset as in step 3

mnist = tf.keras.datasets.fashion_mnist
(training_images, training_labels), (test_images, test_labels) = mnist.load_data()
training_images=training_images/255.0
test_images=test_images/255.0

</pre>

## Define the EarlyStopping callback

<pre class="file" data-filename="step4.py" data-target="append">

callbacks = tf.keras.callbacks.EarlyStopping(
                    monitor='val_accuracy',
                    mode='max', min_delta=0.001,
                    patience = 2)


</pre>

Arguments:
`monitor`: Passing `accuracy` to be monitored in the EarlyStopping callback instance.

`mode` : `max` as we aim for max accuracy. For `loss` it would have been `min`.

`min_delta = 0.001`: 	Minimum change in the monitored quantity to qualify as an improvement, i.e. an absolute change of less than min_delta, will count as no improvement.

`patience`: Number of epochs with no improvement after which training will be stopped.


## Defining the model with the same layers as in Scenario 4.

<pre class="file" data-filename="step4.py" data-target="append">

model = tf.keras.models.Sequential([
  tf.keras.layers.Flatten(),
  tf.keras.layers.Dense(512, activation=tf.nn.relu),
  tf.keras.layers.Dense(10, activation=tf.nn.softmax)
])

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

</pre>


## Passing the callback to the fit() method.

<pre class="file" data-filename="step4.py" data-target="append">

# add a high number(100) of epochs to witness early stopping
model.fit(training_images, training_labels, epochs=100, callbacks=[callbacks])

</pre>

Let's run the script to see what level of accuracy we achieve:

```
python step4.py

```{{execute}}

This is a useful way to fine-tune our model given the concerned performance metric.
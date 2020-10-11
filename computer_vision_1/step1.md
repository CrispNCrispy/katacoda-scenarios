The first step is to get the foundations right. So, we'll start by building a very simple neural network to predict house prices.

So, let's setup our environment first.

Create a new file where our code will reside:

```
touch step1.py
```{{execute}}

Opening the file that we just created `step1.py`{{open}}.

Let's start with imports. 

Here we are importing:
1. `tensorflow` and calling it tf for ease of use.
2. `numpy` which helps us to represent our data as arrays easily and quickly.
3. `keras` framework for defining a neural network as a set of Sequential layers

<pre class="file" data-filename="step1.py" data-target="append">

import tensorflow as tf
import numpy as np
from tensorflow import keras

</pre>

With our environment all set up, we'll try to build a neural network that predicts the price of a house according to a simple formula.

So, imagine we have a very simple house pricing model `50k + 50k per bedroom`, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k and so on. Our goal is to make a model that learns this pricing function from available data and predicts the house prices based on the number of bedrooms.

Let's create some dummy data following the above formula:

<pre class="file" data-filename="step1.py" data-target="append">

bedrooms = np.array([2, 4, 5, 7, 10, 0])
prices = np.array([150, 250, 300, 400, 550, 50])

</pre>

Now, we will create the simplest possible neural network with only 1 layer, and that layer has 1 neuron, and the input shape to it is just 1 value.

<pre class="file" data-filename="step1.py" data-target="append">

model = tf.keras.Sequential([
        keras.layers.Dense(
            units=1,
            input_shape=[1]
            )
        ])

</pre>

Now we compile our Neural Network. When we do so, we have to specify 2 functions, a loss and an optimizer.

The LOSS function measures the guessed answers against the known correct answers and measures how well or how badly it did.

The OPTIMIZER function makes guesses the output. Based on loss function output, it will try to minimize the loss.

We are going to use the stochastic gradient descent `sgd` as the `mean_squared_error` as our loss function for the model.

<pre class="file" data-filename="step1.py" data-target="append">

model.compile(optimizer='sgd', loss='mean_squared_error')

</pre>

The process of training the neural network, where it learns the relationship between the `bedrooms` and `prices` is in the model.fit call.


<pre class="file" data-filename="step1.py" data-target="append">

model.fit(bedrooms, prices, epochs=500)

</pre>

Let's now try to predict the price for an eight bedroom house:


<pre class="file" data-filename="step1.py" data-target="append">

print("Price of the 8-bedroom house is: ", model.predict([10.0]))

</pre>

Finally, let's run the script:

```
python step1.py

```{{execute}}


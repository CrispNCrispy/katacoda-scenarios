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

TensorFlow is a free and open-source software library for dataflow and differentiable programming across a range of tasks. We use Keras, which is a high level API on top of tensorflow. While we can use tensorflow to build neural networks, in most cases, it's sufficient to use Keras without having to understand what's happening under the hood.

<pre class="file" data-filename="step1.py" data-target="append">

import tensorflow as tf
import numpy as np
from tensorflow import keras

</pre>

With our environment all set up, we'll try to build a neural network that predicts the price of a house according to a simple formula.

This is what a neural network looks like:
![](https://miro.medium.com/max/770/1*eJ36Jpf-DE9q5nKk67xT0Q.jpeg)

So, imagine we have a very simple house pricing model `50k + 50k per bedroom`, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k and so on. We can write it using a general notation of **a + bx** where a is 50k, b is 50k and x is the number of bedrooms. Now we could have had many more features, such as square footage which would just extend our general notation to **a + bx + cy** where c is a constant value and y is the square footage. But let's stick to our simple house pricing model for ease of understanding. These unknowns are called the **weights** of the model.

Our goal is to make a model that learns this pricing function from available data and predicts the house prices based on the number of bedrooms. Essentially, the neural network is trying to find of the weight values through an iterative procedure. Once it finds these values, we just need to provide the **x** or the number of bedrooms and it will output the price. 

Let's create some dummy data following the above formula:

<pre class="file" data-filename="step1.py" data-target="append">

bedrooms = np.array([2, 4, 5, 7, 10, 0])
prices = np.array([150, 250, 300, 400, 550, 50])

</pre>

Now, we will create the simplest possible neural network with only 1 layer, and that layer has 1 neuron, and the input shape to it is just 1 value (1 feature).

<pre class="file" data-filename="step1.py" data-target="append">
'''
Sequential() defines a model with a SEQUENCE (stack) of layers in the neural network 

Dense() adds a layer of neurons/nodes

By default, since we are not specifying an activation function, the output is simply going 
to be a linear combination of the inputs - exactly what we want.
'''
model = tf.keras.Sequential([
        keras.layers.Dense(
            units=1,
            input_shape=[1]
            )
        ])

</pre>

If we reference the dense network image above, this is basically one single node in the input layer (which corresponds to number of bedrooms) and one single node in the output layer which is the price of the house. There are no hidden layers in our model as of right now.

Now it's time to compile our Neural Network. When we do so, we have to specify 2 functions, a loss and an optimizer.

The LOSS function measures the guessed answers against the known correct answers and measures how well or how badly it did.

The OPTIMIZER function makes guesses the output. Based on loss function output, it will try to minimize the loss.

We are going to use the stochastic gradient descent `sgd` as the `mean_squared_error` as our loss function for the model. `mean_squared_error` is a very common metric used in linear regression problems involving target variables that are continuous.

<pre class="file" data-filename="step1.py" data-target="append">

model.compile(optimizer='sgd', loss='mean_squared_error')

</pre>

After compiling comes the fitting. The process of training the neural network, where it learns the relationship between the `bedrooms` and `prices` is in the model.fit call. It is iteratively trying to figure out the best weights.


<pre class="file" data-filename="step1.py" data-target="append">

# The number of epochs is the number of passes over the entire dataset done in order to find the best weights.
model.fit(bedrooms, prices, epochs=500)

</pre>

Let's now try to predict the price for an eight bedroom house and obtain the weights of the model.


<pre class="file" data-filename="step1.py" data-target="append">

print("Price of the 8-bedroom house is: ", model.predict([10.0]))
print(model.weights)

</pre>

Finally, let's run the script:

```
python step1.py

```{{execute}}

Notice the values of the weights and how it is very close to 50! This was a small synthetic dataset in which we used the smallest possible neural network. In the next step let's use a real dataset.
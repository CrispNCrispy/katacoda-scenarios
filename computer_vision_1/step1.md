Before we actually move on to working with images, let us first learn how to use Keras and build neural networks for simple problems. We will begin by solving a regression problem in step 1 and 2, and then a classification problem in step 3 and 4.

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

## A hypothetical model
Imagine we have a very simple house pricing model `50k + 50k per bedroom`, so that a 1 bedroom house costs 100k, a 2 bedroom house costs 150k and so on. We can write it using a general notation of **a + bx** where a is 50k, b is 50k and x is the number of bedrooms. Now we could have had many more features, such as square footage which would just extend our general notation to **a + bx + cy** where c is a constant value and y is the square footage. But let's stick to our simple house pricing model for ease of understanding. These unknowns, **a** and **b**, are called the **weights** of the model.

Our goal is to make a model that learns this pricing function from available data and predicts the house prices based on the number of bedrooms. Essentially, the neural network is trying to find the weight values through an iterative procedure. Once it finds these values, we just need to provide the value of **x**, or the number of bedrooms and it will output the price. 

## Data Creation
Let's create some dummy data following the above formula:

<pre class="file" data-filename="step1.py" data-target="append">

bedrooms = np.array([2, 4, 5, 7, 10, 0])
prices = np.array([150, 250, 300, 400, 550, 50])

</pre>

Observe that the data fits our made-up formula. We hope that by using keras, we can create a neural network that will learn it just by providing the data.
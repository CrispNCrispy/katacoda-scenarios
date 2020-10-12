In the previous scenario, we have seen how to create a neural network and how the learnt behaviour solved the problem. We worked with both, a regression problem and a classification problem, using both synthetic data and real data. In some sense, we understood how the outputs were related to the inputs, but what about a problem where writing rules like that is much more difficult -- for example a computer vision problem? 

Here's our next problem where we want to recognize different items of clothing, trained from a dataset containing 10 different types - essentially a classification problem for images rather than data resembling something like the iris dataset.

In an image classification problem, each input corresponds to an image. Each image will consist of a number of features equal to the number of pixels it is made up of. For example, a 32x32 RGB image would have 32x32x3 features.

Create a new file:
```
touch step1.py
```{{execute}}

Opening the file that we just created `step1.py`{{open}}.

Let's start by importing the libraries and make sure you check the version:

<pre class="file" data-filename="step1.py" data-target="append">

import tensorflow as tf
print(tf.__version__)

</pre>

We will train a neural network to recognize items of clothing from a common dataset called Fashion MNIST. You can learn more about this dataset [here](https://www.kaggle.com/zalando-research/fashionmnist).

It contains 70,000 items of clothing in 10 different categories. Each item of clothing is in a 28x28 greyscale image. You can see some examples [here](https://github.com/zalandoresearch/fashion-mnist):

<img src="/orm-harshit-tyagi/scenarios/computer_vision_1/assets/dataset.png" alt="Dataset">

![](/harshit-tyagi/computer_vision_1/assets/dataset.png)

This dataset is also available in the keras datasets API, let's load it:

<pre class="file" data-filename="step1.py" data-target="append">

mnist = tf.keras.datasets.fashion_mnist

</pre>

Likewise, keras (and tensorflow) have plenty of built-in datasets. Next we will extract the data from `mnist`.

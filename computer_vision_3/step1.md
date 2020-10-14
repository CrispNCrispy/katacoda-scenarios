So far we have been working with the Dense layer for classifying images. But in practice, we use a two special layer pair prior to using a Dense layer - a convolution layer and a maximum pooling layer (or an average pooling layer, although newer models all use maximum pooling layers). It's common to see many pairs of convolution layers and maximum pooling layers prior to using dense layers.

When many pairs of these layers are followed by a flatten layer and then a few dense layers, it's commonly called a **Convolution Neural Network (CNN)**. Convolutional neural networks are a kind of feed-forward neural network whose artificial neurons can respond to a part of the surrounding cells in the coverage range - something a dense layer cannot achieve by itself.

Check out the image of a CNN:  
![](https://miro.medium.com/max/1100/1*vkQ0hXDaQv57sALXAJquxA.jpeg)

In this scenario, we will replicate the [LeNet-5](http://yann.lecun.com/exdb/lenet/) convolution nerural network architecure proposed by Yann LeCun et al. in 1998. Since then, we have had much larger and varying types of convolution neural networks, but let's implement this simple architecture and compare its accuracy to our earlier simple dense neural network.

Create a new file where our code will reside:

```
touch step1.py
```{{execute}}

Open the file that we just created `step1.py`{{open}}.

Let's start with imports.

<pre class="file" data-filename="step1.py" data-target="append">

import matplotlib.pyplot as plt
import tensorflow as tf
import numpy as np
from tensorflow.keras.datasets import mnist

</pre>

Let's now load the data from mnist and check out the image and label shapes.

<pre class="file" data-filename="step1.py" data-target="append">

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()
print(train_images.shape)
print(train_labels.shape)
print(test_images.shape)
print(test_labels.shape)

</pre>

Let's execute the code to see the shapes.

```
python step1.py

```{{execute}}

We can see that there are 60,000 images in the training set and 10,000 images in the test set. But there are 2 problems. 
* The first is that a convolution layer expects images in the shape (size, row, width, filters) but ours is just (size, row, width). Since the images are black and white, it represents just 1 filter (in contrast to RGB images, which have 3 filters), but we still need to convert it to a form that can be processed - by increasing the image shape by one dimension.
* The second is that LeNet-5 expects images of size 32x32, but our images are of size 28x28. Two ways we can correct this is to either convert the image into the target size through methods involving stretching of the image or, by padding the images. Padding refers to just adding extra rows and columns that have no meaning - using a value of 0. We shall use the latter method.

We will also have to normalize our pixel values.
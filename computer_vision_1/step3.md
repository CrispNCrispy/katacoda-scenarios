In this, we will repeat what we did, but with a few major changes:
* Bigger Neural Network - 1 hidden layer with multiple nodes.
* Classification Problem - In the previous step, we implemented a regression problem involving a continuous target value. In a classification problem, the target values are discrete finite values such as 0, 1 and 2 or with values in a one-hot encoded format where 2 could be respresented as [0, 0, 1].
* Real Dataset - In this step, we will be working with the famous iris dataset. The dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Each instance also has 4 features this time - sepal length, sepal width, petal length and petal width. In our previous step, we just used one feature - number of bedrooms.
* Splitting our dataset into two parts - a train dataset and a test dataset. We will be reserving 80% of the data for training on the model.fit method and 20% will be used to test the accuracy of the model. The reason we do this is because we want to test the model on data it has not trained on (or not seen), so as to avoid this 'bias'.

Create a new file where our code will reside:

```
touch step3.py
```{{execute}}

Opening the file that we just created `step3.py`{{open}}.

Let's start with imports. 

<pre class="file" data-filename="step3.py" data-target="append">

import tensorflow as tf
import numpy as np
from tensorflow import keras

# For plotting the accuracy and loss over the epochs
import matplotlib.pyplot as plt

# Library which has the dataset built-in
from sklearn.datasets import load_iris

# For splliting our entire data into two parts
from sklearn.model_selection import train_test_split

</pre>

# Loading the dataset
Let's load and view our dataset.

<pre class="file" data-filename="step3.py" data-target="append">

data = load_iris()
X = data['data']
y = data['target']

print(X[:10])
print(y[:10])

</pre>

Execute the dataset to view the first 10 instances.

```
python step3.py

```{{execute}}

The data is already preprocessed, so we do not have to do anything to prepare it and can use it directly. Also we don't really need to care about which column represents what feature - we'll let the model figure out the patterns as only the final target is of relevance to us.

# Splitting the dataset
Let's split our dataset into the training and testing datasets. 

<pre class="file" data-filename="step3.py" data-target="append">

# Split the data into training and testing sets
X_train, X_test, y_train, y_test  = train_test_split(X,y,test_size=0.2)

</pre>

With our data ready, let's work on our model.
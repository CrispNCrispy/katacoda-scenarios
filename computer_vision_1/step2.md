In this, we will repeat what we did, but with a few major changes:
* Bigger Neural Network - 1 hidden layer with multiple nodes.
* Classification Problem - In the previous step, we implemented a regression problem involving a continuous target value. In a classification problem, the target values are discrete finite values such as 0, 1 and 2 or with values in a one-hot encoded format where 2 could be respresented as [0, 0, 1].
* Real Dataset - In this step, we will be working with the famous iris dataset. The dataset contains 3 classes of 50 instances each, where each class refers to a type of iris plant. Each instance also has 4 features this time - sepal length, sepal width, petal length and petal width. In our previous step, we just used one feature - number of bedrooms.
* Splitting our dataset into two parts - a train dataset and a test dataset. We will be reserving 80% of the data for training on the model.fit method and 20% will be used to test the accuracy of the model. The reason we do this is because we want to test the model on data it has not trained on (or not seen), so as to avoid this 'bias'.

Create a new file where our code will reside:

```
touch step2.py
```{{execute}}

Opening the file that we just created `step2.py`{{open}}.

Let's start with imports. 

<pre class="file" data-filename="step2.py" data-target="append">

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

Let's load and view our dataset.

<pre class="file" data-filename="step2.py" data-target="append">

data = load_iris()
X = data['data']
y = data['target']

print(X[:10])
print(y[:10])

</pre>

Execute the dataset to view the first 10 instances.

```
python step2.py

```{{execute}}

The data is already preprocessed, so we do not have to do anything to prepare it and can use it directly. Also we don't really need to care about which column represents what feature - we'll let the model figure out the patterns as only the final target is of relevance to us.

Let's split our dataset, build, compile and fit our model. Pay attention to the comments in the code for an explanation of certain key concepts.

<pre class="file" data-filename="step2.py" data-target="append">

# Split the data into training and testing sets
X_train, X_test, y_train, y_test  = train_test_split(X,y,test_size=0.2)

'''
As mentioned earlier, we are now going to use one hidden layer consisting of 10 nodes.

We will be using a 'relu' activation function for the hidden layer - a popular choice in 
recent ML literature.

We will be using a 'softmax' activation function for the output later because we want
probability values for each class.

We will be using 3 output nodes, with each node's output being a value between 0 and 1, 
which will add up to 1 (because of softmax). Each node will indicate the probability of 
a particular class in the target labels.
'''
model = keras.models.Sequential([
    keras.layers.Dense(units=10, activation='relu', input_shape=(4,)),
    keras.layers.Dense(units=3, activation='softmax')
])



'''
We are using the RMSProp optimizer.

Categorical Cross Entropy is the go to loss function for a classification problem.

It is sparse because our target values are in {0,1,2} instead of one-hot encoded.

We are adding accuracy as metric to be monitored.
'''
model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['accuracy'])



'''
We are providing the test data as the validation_data argument. As a result we'll be able to see the val_loss
and val_accuracy after every epoch.
'''
model.fit(X_train,y_train,epochs=100,validation_data=(X_test,y_test))

</pre>

Let's plot the accuracy and loss values.

<pre class="file" data-filename="step2.py" data-target="append">

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.legend()
plt.savefig('accuracy_plot.png')

plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
plt.legend()
plt.savefig('loss_plot.png')

</pre>

Click `accuracy_plot.png`{{open}} to visualize the accuracy plot.
Click `loss_plot.png`{{open}} to visualize the loss plot.

We can clearly see the accuracy improving and loss decreasing - exactly what we expected. The number of Dense units and the acitvation function in the hidden layer is something that could be changed to obtain better results. We could also add more hidden layers and change the optimizer (or change the learning rate of the optimizer). There is a lot of trial and error that happens when we train a neural network.
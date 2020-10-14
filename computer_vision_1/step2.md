<br>
## Model Creation 
Now, we will create the simplest possible neural network with only 1 layer (output layer), and that layer has 1 neuron/node, and the input shape to it is just 1 value (1 feature).

Open the same file: `step1.py`{{open}}.

<pre class="file" data-filename="step1.py" data-target="append">

model = tf.keras.Sequential([
        keras.layers.Dense(units=1, input_shape=(1,))
        ])

</pre>

* Sequential() defines a model with a SEQUENCE (stack) of layers in the neural network 
* Dense() adds a layer of neurons/nodes
* By default, since we are not specifying an activation function, the output is simply going 
to be a linear combination of the inputs - exactly what we want.

If we look at the dense network image from step 1, the model is basically one single neuron/node in the input layer (which corresponds to number of bedrooms) and one single node in the output layer which is the price of the house. There are no hidden layers in our model as of right now.

## Compiling the model
Now it's time to compile our Neural Network. When we do so, we have to specify 2 arguments, a loss and an optimizer.

* The loss measures the guessed answers against the known correct answers and measures how well or how badly it did.
* The Optimizer guesses the output. Based on loss function output, it will try to minimize the loss.

We are going to use the stochastic gradient descent `sgd` as the `mean_squared_error` as our loss function for the model. `mean_squared_error` is a very common metric used in linear regression problems involving target variables that are continuous.

<pre class="file" data-filename="step1.py" data-target="append">

model.compile(optimizer='sgd', loss='mean_squared_error')

</pre>

## Fitting the model
After compiling comes the fitting. The process of training the neural network, where it learns the relationship between the `bedrooms` and `prices` is in the model.fit call. It is iteratively trying to figure out the best weights.


<pre class="file" data-filename="step1.py" data-target="append">

# The number of epochs is the number of passes over the entire dataset done in order to find the best weights.
model.fit(bedrooms, prices, epochs=500)

</pre>

# Predicting using the model
Let's now try to predict the price for an eight bedroom house and obtain the weights of the model.


<pre class="file" data-filename="step1.py" data-target="append">

print("Price of the 8-bedroom house is: ", model.predict([10.0]))
print(model.weights)

</pre>

Finally, let's run the script:

```
python step1.py

```{{execute}}

Notice the values of the weights (the kernel is the weight associated with the number of bedrroms and the bias is the constant) and how it is very close to 50! This was a small synthetic dataset in which we used the smallest possible neural network. In the next step let's use a real dataset to solve a classification problem.
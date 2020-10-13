
With our training and testing datasets normalized, we are ready to design our model. 

Open the same .py file: `step1`{{open}}

For this model, we'll be using a bunch of layers. Let us also output the summary of the model.

<pre class="file" data-filename="step1.py" data-target="append">

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(input_shape=(28,28)), 
                                    tf.keras.layers.Dense(256, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

print(model.summary())

</pre>

The model is learning over 200k parameters! You can try changing the number of units in the hidden layer (first Dense layer) to see how the number of parameters change. Obviously, the more complex the model, the longer it takes to train.

Let's understand each of these keywords here:

1. **`Sequential`**: That defines a model with a SEQUENCE (stack) of layers in the neural network where each layer has one input tensor and one output tensor.

2. **`Flatten`**: Flatten layer just takes that square and turns it into a 1 dimensional set. For example, if flatten is applied to layer having input shape as (batch_size, 2,2), then the output shape of the layer will be (batch_size, 4)

3. **`Dense`**: Adds a layer of neurons

Each layer of neurons needs an activation function to tell them what to do. There's lots of options, but just use these for now.

**`Relu`** effectively means "If X>0 return X, else return 0" -- so it lets pass values 0 or greater to the next layer in the network.

**`Softmax`** gives us probability for each class that the instance is to be classified into, these add up to 1. For example, if the output from the last layer is [0.0, -1.0, 2.0, 3.0], softmax converts it into [ 0.03467109  0.01275478  0.25618663  0.69638747].


### Compile the Model with optimizer, loss, and metrics.
The next thing to do, now the model is defined, is to actually build it. We do this by compiling it with an optimizer and loss function.

<pre class="file" data-filename="step1.py" data-target="append">

model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

</pre>

We are using one of the most popular optimizers - the Adam optimizer. Since it is a classification problem with labels not in a one-hot encoded format, we use a sparse categorical entropy loss.
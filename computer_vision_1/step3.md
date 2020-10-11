
With our training and testing datasets normalized, we are ready to design our model. 

Let's use the same `step2`{{open}} file with the normalization code in it.

For this model, we'll be using a bunch of layers, here's our model:

<pre class="file" data-filename="step2.py" data-target="append">

model = tf.keras.models.Sequential([tf.keras.layers.Flatten(), 
                                    tf.keras.layers.Dense(128, activation=tf.nn.relu), 
                                    tf.keras.layers.Dense(10, activation=tf.nn.softmax)])

</pre>

Let's understand each of these keywords here:

1. **`Sequential`**: That defines a model with a SEQUENCE(stack) of layers in the neural network where each layer has one input tensor and one output tensor.

2. **`Flatten`**: Flatten layer just takes that square and turns it into a 1 dimensional set. For example, if flatten is applied to layer having input shape as (batch_size, 2,2), then the output shape of the layer will be (batch_size, 4)

3. **`Dense`**: Adds a layer of neurons

Each layer of neurons needs an activation function to tell them what to do. There's lots of options, but just use these for now.

**`Relu`** effectively means "If X>0 return X, else return 0" -- so it lets pass values 0 or greater to the next layer in the network.

**`Softmax`** gives us probability for each class that the instance is to be classified into, these add up to 1. For example, if the output from the last layer is [0.0, -1.0, 2.0, 3.0], softmax converts it into [ 0.03467109  0.01275478  0.25618663  0.69638747].


### Compile the Model with optimizer, loss, and metrics.
The next thing to do, now the model is defined, is to actually build it. We do this by compiling it with an optimizer and loss function.

<pre class="file" data-filename="step2.py" data-target="append">

model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

</pre>


## Train the model by invoking the `fit()` method.

<pre class="file" data-filename="step2.py" data-target="append">

model.fit(train_images, train_labels, epochs=5)

</pre>

Once it's done training -- you should see an accuracy value at the end of the final epoch. It might look something like 0.9098. This tells you that your neural network is about 91% accurate in classifying the training data.

You should try to see if you can improve the performance by changing the number of epochs.


### Evaluating the Model.
To evaluate a model, we should know how it performs on unseen data. That's why we have test images. We'll use `model.evaluate()` and pass the test images and labels to it:

<pre class="file" data-filename="step2.py" data-target="append">

model.evaluate(test_images, test_labels)

</pre>


Let's run the script and check out how our model performs:

```
python step2.py

```{{execute}}

For me, that returned a accuracy of about .8838, which means it was about 88% accurate. As expected it probably would not do as well with unseen data as it did with data it was trained on! In the next step, we'll find ways to improve upon this.
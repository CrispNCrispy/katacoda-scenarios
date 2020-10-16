It is now time to build, compile and fit our model.

## Creating the model
* As mentioned earlier, we are now going to use one hidden layer consisting of 10 nodes.
* We will be using a `relu` activation function for the hidden layer - a popular choice in 
recent ML literature.
* We will be using a `softmax` activation function for the output later because we want
probability values for each class.
* We will be using 3 output nodes, with each output being a value between 0 and 1, 
which will add up to 1 (because of softmax). Each node will indicate the probability of 
a particular class in the target labels.

<pre class="file" data-filename="step3.py" data-target="append">

model = keras.models.Sequential([
    keras.layers.Dense(units=10, activation='relu', input_shape=(4,)),
    keras.layers.Dense(units=3, activation='softmax')
])

# View the model summary
print(model.summary())

</pre>

Let's execute the code to view the summary of the model we are creating.

```
python step3.py

```{{execute}}

Notice the number of parameters for each layer. These are the `weights` or the `unknowns` that the model attempts to find through `Backpropagation` - an algorithm that is used to compute the gradients of a neural network to reach a point of minimization of the cost function (or loss function) such as the `mean squared error (MSE)` that we used in Step 2, or the loss function we are going to use in the very next code block.

## Compiling the model
* We are going to use the RMSProp optimizer.
* Categorical Cross Entropy is the go to loss function for a classification problem.
* It is sparse because our target values are in {0,1,2} instead of one-hot encoded.
* We are adding accuracy as a metric to be monitored.

<pre class="file" data-filename="step3.py" data-target="append">

model.compile(optimizer='rmsprop',loss='sparse_categorical_crossentropy',metrics=['accuracy'])

</pre>

## Fitting the model
* We are providing the test data as the validation_data argument. As a result we will be able to see the `val_loss` and `val_accuracy` (test set loss and accuracy) after every epoch.

<pre class="file" data-filename="step3.py" data-target="append">

model.fit(X_train,y_train,epochs=100,validation_data=(X_test,y_test))

</pre>

## Plotting

Let's also add the code block to plot the accuracy and loss values over the epochs.

<pre class="file" data-filename="step3.py" data-target="append">

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.legend()
plt.savefig('accuracy_plot.png')

plt.close()
plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.legend()
plt.savefig('loss_plot.png')

</pre>

Execute the code to view the output and the plots.

```
python step3.py

```{{execute}}

Click `accuracy_plot.png`{{open}} to visualize the accuracy plot.
Click `loss_plot.png`{{open}} to visualize the loss plot.

* We can clearly see the accuracy improving and loss decreasing - exactly what we expected. 
* The number of Dense units and the activation function in the hidden layer is something that could be changed to obtain better results. We could also add more hidden layers and change the optimizer (or change the learning rate of the optimizer). There is a lot of trial and error that happens when we train a neural network.

In the next scenario, we'll be putting all of what we learnt to classify image data!
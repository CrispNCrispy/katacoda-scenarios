<br>
## Train the model by invoking the `fit()` method.
Open the same .py file: `step1.py`{{open}}

<pre class="file" data-filename="step1.py" data-target="append">

model.fit(train_images, train_labels, epochs=5, validation_data=(test_images,test_labels))

</pre>

## Plotting
Let's plot the accuracy and loss values.

<pre class="file" data-filename="step1.py" data-target="append">

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

### Evaluating the Model.
To evaluate a model, we should know how it performs on unseen data. That's why we have test images. We'll use `model.evaluate()` and pass the test images and labels to it:

<pre class="file" data-filename="step1.py" data-target="append">

model.evaluate(test_images, test_labels)

</pre>

Execute the code to view the output and the plots.

```
python step1.py

```{{execute}}

Once it's done training -- you should see an accuracy value at the end of the final epoch. For me, that returned an accuracy of about 0.8945 (89.45%) for the training set and 0.8797 (87.97%) for the test set. You can expect something similar (the exact value will differ with different runs). The reason it differs with different runs is because the weights of Dense layers are initialized randomly. One way to initialize it with the same values all the time (in case if you are curious) is to use the seed argument to any int value when using the initializer argument in a layer. For example, `tf.keras.layers.Dense(256, activation=tf.nn.relu, kernel_initializer=tf.keras.initializers.GlorotUniform(seed=5))`. GlorotUniform is the default kernel initializer for the dense layer. We do not need to specify a seed for the bias_initializer because by default it sets all the bias values to zero.

You should try to see if you can improve the performance by changing the number of epochs or any other hyperparamters such as the optimizer, the optimizer's learning rate, etc.

* Click `accuracy_plot.png`{{open}} to visualize the accuracy plot. Both the train and test accuracy are increasing - as expected.  
* Click `loss_plot.png`{{open}} to visualize the loss plot. Both the train and test loss are decreasing - as expected.

As expected it probably would not do as well with unseen data as it did with data it was trained on!
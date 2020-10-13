## Train the model by invoking the `fit()` method.

Open the same .py file: `step1`{{open}}

<pre class="file" data-filename="step1.py" data-target="append">

model.fit(train_images, train_labels, epochs=5, validation_data=(test_images,test_labels))

</pre>

Once it's done training -- you should see an accuracy value at the end of the final epoch. It might look something like 0.9098. This tells you that your neural network is about 91% accurate in classifying the training data.

You should try to see if you can improve the performance by changing the number of epochs.

## Plotting

Let's plot the accuracy and loss values.

<pre class="file" data-filename="step1.py" data-target="append">

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.legend()
plt.savefig('accuracy_plot.png')

plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
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

Click `accuracy_plot.png`{{open}} to visualize the accuracy plot.
Click `loss_plot.png`{{open}} to visualize the loss plot.

For me, that returned a accuracy of about .8945 (89.45%) for the training set and 0.8797 (87.97%) for the test set. As expected it probably would not do as well with unseen data as it did with data it was trained on!
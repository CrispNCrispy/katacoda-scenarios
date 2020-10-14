## Train the model by invoking the `fit()` method.
It's time to train the model. We will be using the batch_size argument, meaning that we will be fitting on 16 images at a time - as we don't want to flood our memory. The training may take some time.

Open the same .py file: `step1`{{open}}

<pre class="file" data-filename="step1.py" data-target="append">

model.fit(train_images, train_labels, epochs=5, batch_size=1024, validation_data=(test_images,test_labels))

</pre>

You should later try to see if you can improve the performance by changing certain hyperparameters like number of epochs or the optimizer, etc.

## Plotting
Let's plot the accuracy and loss values.

<pre class="file" data-filename="step1.py" data-target="append">

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.savefig('accuracy_plot.png')

plt.close()
plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Loss')
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

Wow, I received a training accuracy of 0.9919 (99.19%) and a test accuracy of 0.9873 (98.73%)! That is a massive improvement, and we even reduced the number of parameters to learn!
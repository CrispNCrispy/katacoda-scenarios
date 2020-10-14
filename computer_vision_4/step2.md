<br>
## Compiling, Fitting and Plotting the model
Let's now compile, fit the model and plot it to view what happened. We add the callback in the `model.fit` method

<pre class="file" data-filename="step1.py" data-target="append">

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

# add a high number(100) of epochs to witness early stopping
model.fit(training_images, training_labels, validation_data=(test_images,test_labels), epochs=100, callbacks=[callback1], batch_size=1024)

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.savefig('accuracy_plot_1.png')

plt.close()
plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.savefig('loss_plot_1.png')

</pre>

Execute the code to view the output and the plots. This may take some time - so grab a cup of coffee or read something while you wait!

```
python step1.py

```{{execute}}

* Click `accuracy_plot_1.png`{{open}} to visualize the accuracy plot.
* Click `loss_plot_1.png`{{open}} to visualize the loss plot.

You can see that as the model's accuracy started to decrease after reaching the maximum, the EarlyStopping callback allowed the model to stop at that point.
<br>
## Compiling, Fitting and Plotting the model
Let's now compile, fit the model and plot it to view what happens. Also check out the learning rate parameter in the Adam optimizer in the compile method.

Open the file: `step3.py`{{open}}.

<pre class="file" data-filename="step3.py" data-target="append">

# compile the model
model.compile(optimizer=tf.keras.optimizers.Adam(learning_rate=0.001), loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(training_images, training_labels, validation_data=(test_images,test_labels), epochs=30, callbacks=[callback2], batch_size=1024)

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.savefig('accuracy_plot_2.png')

plt.close()
plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
plt.legend()
plt.xlabel('Epochs')
plt.ylabel('Loss')
plt.savefig('loss_plot_2.png')

</pre>

Execute the code to view the output and the plots. Look at the `model.fit()` outputs and how the learning rate decreases based on the scheduler function.

```
python step3.py

```{{execute}}

* Click `accuracy_plot_2.png`{{open}} to visualize the accuracy plot.
* Click `loss_plot_2.png`{{open}} to visualize the loss plot.
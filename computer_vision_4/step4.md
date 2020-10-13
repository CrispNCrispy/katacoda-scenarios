### Compiling, Fitting and Plotting the model
Let's now compile, fit the model and plot it to view what happened

<pre class="file" data-filename="step3.py" data-target="append">

# compile the model
model.compile(optimizer='adam', loss='sparse_categorical_crossentropy', metrics=['accuracy'])

model.fit(training_images, training_labels, validation_data=(test_images,test_labels), epochs=30, callbacks=[callback2], batch_size=1024)

plt.plot(model.history.history['accuracy'],label='Train Accuracy')
plt.plot(model.history.history['val_accuracy'],label='Test Accuracy')
plt.legend()
plt.savefig('accuracy_plot_2.png')

plt.plot(model.history.history['loss'],label='Train Loss')
plt.plot(model.history.history['val_loss'],label='Test Loss')
plt.legend()
plt.savefig('loss_plot_2.png')

</pre>

Execute the code to view the output and the plots. Look at model.fit outputs and how the learning rate decreases based on the scheduler function.

```
python step3.py

```{{execute}}

Click `accuracy_plot_2.png`{{open}} to visualize the accuracy plot.
Click `loss_plot_2.png`{{open}} to visualize the loss plot.
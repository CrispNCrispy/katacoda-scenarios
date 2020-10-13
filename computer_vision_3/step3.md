## Model Creation
The '5' in LeNet-5 corresponds to 5 layers - or rather 5 trainable layers (Max Pooling layers and Flatten layers have no trainable parameters). The following are the layers:
1. Convolution Layer 1 + Avg. Pool Layer 1
2. Convolution Layer 2 + Avg. Pool Layer 2
3. Flatten Layer + Dense Layer 1
4. Dense Layer 2
5. Dense Layer 3 (Output layer)

Open the same fle to continue: `step1.py`{{open}}.

For this model, we'll be using a bunch of layers. After creating it, view the model.summart() to view the number of parameters.

<pre class="file" data-filename="step1.py" data-target="append">

model = tf.keras.Sequential([
    tf.keras.layers.Conv2D(filters=6, kernel_size=(3, 3), activation='relu', input_shape=(32,32,1)),
    tf.keras.layers.AveragePooling2D(),
    tf.keras.layers.Conv2D(filters=16, kernel_size=(3, 3), activation='relu'),
    tf.keras.layers.AveragePooling2D(),
    tf.keras.layers.Flatten(),
    tf.keras.layers.Dense(units=120, activation='relu'),
    tf.keras.layers.Dense(units=84, activation='relu'),
    tf.keras.layers.Dense(units=10, activation='softmax')
])

print(model.summary())

</pre>

Execute the code to see the model summary.

```
python step1.py

```{{execute}}

The model has just over 81k parameters compared to 200k in the last scenario! But will it get a higher accuracy? Let's find out.

### Compile the Model with optimizer, loss, and metrics.
The next thing to do, now the model is defined, is to actually build it. We do this by compiling it with an optimizer and loss function.

<pre class="file" data-filename="step1.py" data-target="append">

model.compile(optimizer = tf.keras.optimizers.Adam(),
              loss = 'sparse_categorical_crossentropy',
              metrics=['accuracy'])

</pre>

Let's now move on to fitting and evalutating the model.
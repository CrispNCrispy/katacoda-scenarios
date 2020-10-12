## Train the model by invoking the `fit()` method.

Open the same .py file: `step1`{{open}}

<pre class="file" data-filename="step1.py" data-target="append">

model.fit(train_images, train_labels, epochs=5)

</pre>

Once it's done training -- you should see an accuracy value at the end of the final epoch. It might look something like 0.9098. This tells you that your neural network is about 91% accurate in classifying the training data.

You should try to see if you can improve the performance by changing the number of epochs.


### Evaluating the Model.
To evaluate a model, we should know how it performs on unseen data. That's why we have test images. We'll use `model.evaluate()` and pass the test images and labels to it:

<pre class="file" data-filename="step1.py" data-target="append">

model.evaluate(test_images, test_labels)

</pre>

Alternative to using the model.evaluate() method, we could have provided the test data as the 'validation_data' argument in the model.fit() method - which would output test data based metrics during the fitting.

Let's run the script and check out how our model performs:

```
python step1.py

```{{execute}}

For me, that returned a accuracy of about .8838, which means it was about 88% accurate. As expected it probably would not do as well with unseen data as it did with data it was trained on!
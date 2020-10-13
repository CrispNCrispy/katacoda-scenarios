## Train the model by invoking the `fit()` method.
It's time to train the model. We will be using the batch_size argument, meaning that we will be fitting on 16 images at a time - as we don't want to flood our memory. The training may take some time.

Open the same .py file: `step1`{{open}}

<pre class="file" data-filename="step1.py" data-target="append">

model.fit(train_images, train_labels, epochs=5, batch_size=16)

</pre>

You should later try to see if you can improve the performance by changing certain hyperparameters like epoch, or the optimizer, etc.


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

Wow, I received a training accuracy of 0.9919 (99.19%) and a test accuracy of 0.9873 (98.73%)! That is a massive improvement, and we even reduced the number of parameters to learn!
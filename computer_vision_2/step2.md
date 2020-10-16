<br>
## In-built split of the dataset
Calling the `load_data` method on the `mnist` object will give you two sets of two lists, these will be the training and testing values for the graphics that contain the clothing items and their labels.

<pre class="file" data-filename="step1.py" data-target="append">

(train_images, train_labels), (test_images, test_labels) = mnist.load_data()

</pre>

## Normalize image data
All the pixels are basically values in the range 0 to 255. If we are training a neural network, for various reasons it's easier if we treat all values as between 0 and 1. Therefore, we'll have to normalize the images by dividing each one of the training and testing images by 255:


<pre class="file" data-filename="step1.py" data-target="append">

print("Few pixel values BEFORE normalization: \n", train_images[0,20:30,20:30])
train_images  = train_images / 255.0
test_images = test_images / 255.0
print("\nFew pixel values AFTER normalization: \n", train_images[0,20:30,20:30])

</pre>

Let's run the script to view some of the pixel values:

```
python step1.py

```{{execute}}

Notice that the pixel values went from the range of 0-255 to 0-1. This simple `Feature Scaling` is not the only way of normalization, but this simple way of dividing by 255 is very common for image pixels.

Normalization is a key step in any machine learning problem. We would like all values to be within the same small range in order for the optimizer to work more efficiently.
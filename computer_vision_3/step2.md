<br>
## Data Normalization
A common (and necessary) practice is to normalize our pixel values by dividing it by 255 to get it in the 0-1 range. This helps our optimizer achieve minimization faster.

Open the same fle to continue: `step1.py`{{open}}.

<pre class="file" data-filename="step1.py" data-target="append">

print("Few pixel values BEFORE normalization: \n", train_images[0,20:26,20:26])
train_images  = train_images / 255.0
test_images = test_images / 255.0
print("\nFew pixel values AFTER normalization: \n", train_images[0,20:26,20:26])

</pre>

Let's run the script to view some of the pixel values:

```
python step1.py

```{{execute}}

Notice that the pixel values went from the range of 0-255 to 0-1. This simple `Feature Scaling` is not the only way of normalization, but this simple way of dividing by 255 is very common for image pixels.

## Dimension Expansion
As mentioned in the last step, we need to change our images matrix to (size, 28, 28, 1) instead of (size, 28, 28). To do this, we will use the `np.expand_dims()` function.


<pre class="file" data-filename="step1.py" data-target="append">

train_images = np.expand_dims(train_images,-1)
test_images = np.expand_dims(test_images,-1)

</pre>

## Data Padding
LeNet-5 expects our image sizes to be 32x32 as in the [original paper](http://yann.lecun.com/exdb/publis/pdf/lecun-01a.pdf). We could change the input size to 28x28 but let's stick with the original model. In order to do this, we will pad our 28x28 images with zeros to get it to 32x32, i.e., add 4 rows of zeros (2 above the image and 2 below) and 4 columns of zeros (2 to the left of the image and 2 to the right of the image).

<pre class="file" data-filename="step1.py" data-target="append">

train_images = np.pad(train_images, ((0,0),(2,2),(2,2),(0,0)), 'constant')
test_images = np.pad(test_images, ((0,0),(2,2),(2,2),(0,0)), 'constant')

</pre>

With our code for the data preparation ready, let's move on to creating and compiling our model.
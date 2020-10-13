## Data Normalization
A common (and necessary) practice is to normalize our pixel values by dividing it by 255 to get it in the 0-1 range. This helps our optimizer achieve minimization faster.

Open the same fle to continue: `step1.py`{{open}}.

<pre class="file" data-filename="step1.py" data-target="append">

print("Pixel values BEFORE normalization: ", train_images[0])
train_images  = train_images / 255.0
test_images = test_images / 255.0
print("Pixel values AFTER normalization: ", train_images[0])

</pre>

## Dimension Expansion
As mentioned in the last step, we need to change our images matrix to (size, 28, 28, 1) instead of (size, 28, 28). To do this, we will use the `np.expand_dims()` function.


<pre class="file" data-filename="step1.py" data-target="append">

train_images = np.expand_dims(train_images,-1)
test_images = np.expand_dims(test_images,-1)

</pre>

## Data Padding
LeNet-5 expects our image sizes to be 32x32. In order to do this, we will pad our images with zeros, i.e., add 4 rows of zeros (2 above the image and 2 below) and 4 columns of zeros (2 to the left of the image and 2 to the right of the image).

<pre class="file" data-filename="step1.py" data-target="append">

train_images = np.pad(train_images, ((0,0),(2,2),(2,2),(0,0)), 'constant')
test_images = np.pad(test_images, ((0,0),(2,2),(2,2),(0,0)), 'constant')

</pre>

With our code for the data preparation ready, let's move on to creating and compiling our model.